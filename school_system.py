from models import *
from flask import Flask, request, g, redirect, url_for, render_template, session
from administrator import AdministratorData
from mentors import MentorsData
from applicants import ApplicantsData
import datetime


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DEBUG=True, SECRET_KEY='any_random_string'))

administrator_data = AdministratorData()
applicants_data = ApplicantsData()
mentors_data = MentorsData()

app.config.from_envvar('SUPER_SPRINTER_3000_SETTINGS', silent=True)


def init_db():
    identify = open("parameter.txt", "r")
    login = identify.readlines()
    identify.close()
    db = PostgresqlDatabase(login[0], user=login[0])
    try:
        db.connect()
        print("Database connection established.")
    except:
        print("Can't connect to database.\nPlease check your connection.txt file.")


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'postgre_db'):
        g.postgre_db.close()


@app.route('/')
def home_menu():

    if 'admin' in session:
        return redirect(url_for('admin_menu'))
    elif 'mentor' in session:
        return redirect(url_for('mentor_menu'))
    elif 'applicant' in session:
        return redirect(url_for('applicant_menu'))
    else:
        return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return redirect(url_for('home_menu'))

    else:
        try:
            user = User.select().where(
                (User.email == request.form['user-name']) & (User.password == request.form['password'])).get()

            if user is not None:
                if 'admin' or 'applicant' or 'mentor' not in session:

                    if user.user_status == 1:
                        session['admin'] = user.email
                        return redirect(url_for('admin_menu'))

                    elif user.user_status == 2:
                        session['mentor'] = user.email
                        return redirect(url_for('mentor_menu'))

                    else:
                        session['applicant'] = user.email
                        return redirect(url_for('applicant_menu'))
            else:
                return redirect(url_for('home_menu'))
        except:
            return redirect(url_for('new_applicant_form'))


@app.route('/admin/admin_menu')
def admin_menu():
    if 'admin' in session:
        return render_template('admin_menu.html')

    else:
        return redirect(url_for('home_menu'))


@app.route('/logout')
def logout():
    if 'admin' or 'applicant' or 'mentor' in session:
        session.pop('admin', None)
        return render_template('home.html')
    else:
        return redirect(url_for('home_menu'))


@app.route('/applicant_menu')
def applicant_menu():
    if 'applicant' in session:
        return render_template('applicant_menu.html')
    else:
        return redirect(url_for('home_menu'))

@app.route('/mentor_menu')
def mentor_menu():
    if 'mentor' in session:
        return render_template('mentor_menu.html')
    else:
        return redirect(url_for('home_menu'))


@app.route('/applicant/personal_data')
def applicant_personal_data():
    applicants_data.get_applicant_personal_data()
    table_header = applicants_data.tags
    table_content = applicants_data.results
    return render_template('applicant_data.html', header=table_header, content=table_content)


@app.route('/new_applicant_form')
def new_applicant_form():

    cities = City.select().order_by(City.id.asc())
    return render_template('register_applicant.html', cities=cities)


@app.route('/registration', methods=['POST'])
def registration():

    applicants_data.new_applicant(city_input=request.form["city"], name_input=request.form[
        "name"], email_input=request.form["email"])
    return render_template('home.html')


@app.route('/admin/applicant_list')
def listing_all_applicants():

    if 'admin' in session:
        administrator_data.listing_all_applicants()
        table_header = administrator_data.tags
        table_content = administrator_data.results
        return render_template('all_applicants.html', header=table_header, content=table_content)
    elif 'mentor' in session:
        return redirect(url_for('mentor_menu'))
    elif 'applicant' in session:
        return redirect(url_for('applicant_menu'))
    else:
        return redirect(url_for('home_menu'))


@app.route('/admin/interview_list')
def listing_all_interviews():

    if 'admin' in session:
        administrator_data.listing_all_interviews()
        table_header = administrator_data.tags
        table_content = administrator_data.results
        return render_template('all_interviews.html', header=table_header, content=table_content)

    else:
        return redirect(url_for('home_menu'))


@app.route('/admin/applicant_list', methods=["POST"])
def filter_applicants():

    if 'admin' in session:
        if request.form["filter_by"] == "Status":
            administrator_data.applicants_by_status(request.form["filter"])
            table_header = administrator_data.tags
            table_content = administrator_data.results
        elif request.form["filter_by"] == "Interview":
            try:
                filter_transfer = datetime.datetime.strptime(
                    request.form["filter"], '%Y-%m-%d')
            except ValueError:
                table_header = ["ERROR: wrong date format"]
                table_content = [
                    ["Please give the interview's date in the following format: 2015-01-01"]]
            else:
                administrator_data.applicants_by_interview(
                    request.form["filter"])
                table_header = administrator_data.tags
                table_content = administrator_data.results
        elif request.form["filter_by"] == "School":
            administrator_data.applicants_by_location(request.form["filter"])
            table_header = administrator_data.tags
            table_content = administrator_data.results
        elif request.form["filter_by"] == "City":
            administrator_data.applicants_by_city(request.form["filter"])
            table_header = administrator_data.tags
            table_content = administrator_data.results
        elif request.form["filter_by"] == "Mentor":
            administrator_data.applicants_by_mentor(request.form["filter"])
            table_header = administrator_data.tags
            table_content = administrator_data.results
        elif request.form["filter_by"] == "Code":
            administrator_data.applicant_email_by_applicant_code(request.form[
                "filter"])
            table_header = administrator_data.tags
            table_content = administrator_data.results
        return render_template('all_applicants.html', header=table_header, content=table_content)

    else:
        return redirect(url_for('home_menu'))


@app.route('/admin/e-mail-log')
def listing_all_emails():

    if 'admin' in session:
        administrator_data.listing_all_emails()
        table_header = administrator_data.tags
        table_content = administrator_data.results
        return render_template('email_list.html', header=table_header, content=table_content)

    else:
        return redirect(url_for('home_menu'))


@app.route('/admin/interview_list', methods=["POST"])
def filter_interviews():

    if 'admin' in session:
        if request.form["filter_by"] == "School":
            administrator_data.listing_interviews_by_school(
                request.form["filter"])
            table_header = administrator_data.tags
            table_content = administrator_data.results
        elif request.form["filter_by"] == "Applicant code":
            administrator_data.listing_interviews_by_applicant_code(request.form[
                                                                    "filter"])
            table_header = administrator_data.tags
            table_content = administrator_data.results
        elif request.form["filter_by"] == "Mentor":
            administrator_data.listing_interviews_by_mentor(
                request.form["filter"])
            table_header = administrator_data.tags
            table_content = administrator_data.results
        elif request.form["filter_by"] == "Date":
            try:
                filter_transfer = datetime.datetime.strptime(
                    request.form["filter"], '%Y-%m-%d')
            except ValueError:
                table_header = ["ERROR: wrong date format"]
                table_content = [
                    ["Please give the interview's date in the following format: 2015-01-01"]]
            else:
                administrator_data.listing_interviews_by_date(
                    request.form["filter"])
                table_header = administrator_data.tags
                table_content = administrator_data.results
        return render_template('all_interviews.html', header=table_header, content=table_content)

    else:
        return redirect(url_for('home_menu'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0')
