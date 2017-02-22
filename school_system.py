from models import *
from flask import Flask, request, g, redirect, url_for, \
    render_template
from administrator import AdministratorData
from mentors import MentorsData
from applicants import ApplicantsData
import datetime


DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

administrator_data = AdministratorData()
applicants_data = ApplicantsData()
mentors_data = MentorsData()


def init_db():
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
def main_menu():
    return render_template('admin_menu.html')


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
    table_content = administrator_data.query
    return render_template('all_applicants.html', header=table_header, content=table_content)


@app.route('/admin/interview_list')
def listing_all_interviews():
    administrator_data.listing_all_interviews()
    table_header = administrator_data.tags
    table_content = administrator_data.results
    return render_template('all_interviews.html', header=table_header, content=table_content)

@app.route('/admin/e-mail-log')
def listing_all_emails():
    administrator_data.listing_all_emails()
    table_header = administrator_data.tags
    table_content = administrator_data.query
    return render_template('email_list.html', header=table_header, content=table_content)

@app.route('/admin/interview_list', methods=["POST"])
def filter_interviews():
    if request.form["filter_by"] == "School":
        administrator_data.listing_interviews_by_school(request.form["filter"])
        table_header = administrator_data.tags
        table_content = administrator_data.results
    elif request.form["filter_by"] == "Applicant code":
        administrator_data.listing_interviews_by_applicant_code(request.form["filter"])
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
            administrator_data.listing_interviews_by_date(request.form["filter"])
            table_header = administrator_data.tags
            table_content = administrator_data.results
    return render_template('all_interviews.html', header=table_header, content=table_content)


if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0')
