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


def init_db():
    db = PostgresqlDatabase('dry', user='dry')
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
    return render_template('home.html')


@app.route('/login')
def login():

    USERNAME = 'adminus'
    PASSWORD = 'adminpass'

    name_error = 'Invalid username!'
    password_error = 'Invalid password!'

    if request.method == 'POST':

        if 'admin' not in session:

            if USERNAME != request.form['user-name']:
                return redirect(url_for('login', error=name_error))
            elif PASSWORD != request.form['password']:
                return redirect(url_for('login', error=password_error))
            else:
                session['admin'] = request.form['user-name']
                return redirect(url_for('admin_menu'))
        else:
            redirect(url_for('/'))


    else:
        return redirect('/')

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('admin', None)
    return redirect(url_for('main_menu'))


@app.route('/applicant_registration')
def new_applicant_form():
    cities = City.select().order_by(City.id.asc())
    return render_template('register_applicant.html', cities=cities)


@app.route('/registration', methods=['POST'])
def new_applicant_registration():
    applicants_data.new_applicant(city_input=request.form["city"], name_input=request.form[
        "name"], email_input=request.form["email"])
    return redirect('/')


@app.route('/admin/applicant_list')
def listing_all_applicants():
    administrator_data.listing_all_applicants()
    table_header = administrator_data.tags
    table_content = administrator_data.results
    return render_template('all_applicants.html', header=table_header, content=table_content)


@app.route('/admin/interview_list')
def listing_all_interviews():
    administrator_data.listing_all_interviews()
    table_header = administrator_data.tags
    table_content = administrator_data.query
    return render_template('all_interviews.html', header=table_header, content=table_content)


@app.route('/admin/applicant_list', methods=["POST"])
def filter_applicants():
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
            administrator_data.applicants_by_interview(request.form["filter"])
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


@app.route('/admin/e-mail-log')
def listing_all_emails():
    administrator_data.listing_all_emails()
    table_header = administrator_data.tags
    table_content = administrator_data.query
    return render_template('email_list.html', header=table_header, content=table_content)


if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0')
