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
    admin_message = 'ADMIN MODE IS ON'
    return render_template('home.html', message=admin_message)


@app.route('/login', methods=['GET', 'POST'])
def login():

    USERNAME = 'admin'
    PASSWORD = 'admin'

    name_error = 'Invalid username!'
    password_error = 'Invalid password!'
    admin_message = 'ADMIN MODE IS ON'

    if request.method == 'POST':

        if 'admin' not in session:

            if USERNAME != request.form['user-name']:
                return render_template('home.html', error=name_error)
            elif PASSWORD != request.form['password']:
                return render_template('home.html', error=password_error)
            elif request.form['role'] != 'administrator':
                # purposeful password error
                return render_template('home.html', error=password_error)
            else:
                session['admin'] = request.form['user-name']
                return render_template('admin_menu.html', message=admin_message)
        else:
            return render_template('admin_menu', message=admin_message)

    else:
        return redirect(url_for('home_menu'))


@app.route('/admin_menu', methods=['GET'])
def admin_menu():
    admin_message = 'ADMIN MODE IS ON'
    return render_template('/admin_menu.html', message=admin_message)


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('admin', None)
    return render_template('home.html')


@app.route('/applicant_registration')
def new_applicant_form():
    admin_message = 'ADMIN MODE IS ON'
    cities = City.select().order_by(City.id.asc())
    return render_template('register_applicant.html', cities=cities, message=admin_message)


@app.route('/registration', methods=['POST'])
def new_applicant_registration():
    admin_message = 'ADMIN MODE IS ON'
    applicants_data.new_applicant(city_input=request.form["city"], name_input=request.form[
        "name"], email_input=request.form["email"])
    return render_template('home.html', message=admin_message)


@app.route('/admin/applicant_list')
def listing_all_applicants():
    if 'admin' in session:
        administrator_data.listing_all_applicants()
        table_header = administrator_data.tags
        table_content = administrator_data.results
        return render_template('all_applicants.html', header=table_header, content=table_content)
    else:
        return redirect(url_for('new_applicant_form'))


@app.route('/admin/interview_list')
def listing_all_interviews():

    if 'admin' in session:
        administrator_data.listing_all_interviews()
        table_header = administrator_data.tags
        table_content = administrator_data.results
        return render_template('all_interviews.html', header=table_header, content=table_content)
    else:
        return redirect(url_for('new_applicant_form'))


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
        return redirect(url_for('new_applicant_form'))


@app.route('/admin/e-mail-log')
def listing_all_emails():
    administrator_data.listing_all_emails()
    table_header = administrator_data.tags
    table_content = administrator_data.results
    return render_template('email_list.html', header=table_header, content=table_content)


@app.route('/admin/interview_list', methods=["POST"])
def filter_interviews():
    if 'admin' in session:
        if request.form["filter_by"] == "School":
            administrator_data.listing_interviews_by_school(request.form["filter"])
            table_header = administrator_data.tags
            table_content = administrator_data.results
        elif request.form["filter_by"] == "Applicant code":
            administrator_data.listing_interviews_by_applicant_code(request.form[
                                                                    "filter"])
            table_header = administrator_data.tags
            table_content = administrator_data.results
        elif request.form["filter_by"] == "Mentor":
            administrator_data.listing_interviews_by_mentor(request.form["filter"])
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
        return redirect(url_for('new_applicant_form'))

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0')
