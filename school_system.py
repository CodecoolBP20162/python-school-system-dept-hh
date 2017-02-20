from models import *
from flask import Flask, request, g, redirect, url_for, \
    render_template
from administrator import AdministratorData
from mentors import MentorsData
from applicants import ApplicantsData


DEBUG = True

app = Flask(__name__, static_url_path="/templates", static_folder="templates")
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
    return render_template('main.html')


@app.route('/applicant_registration')
def new_applicant_form():
    cities = City.select().order_by(City.id.asc())
    return render_template('registration.html', cities=cities)


@app.route('/registration', methods=['POST'])
def new_applicant_registration():
    applicants_data.new_applicant(city_input=request.form["city"], name_input=request.form[
        "name"], email_input=request.form["email"])
    return redirect('new_applicant_form')


@app.route('/admin/applicant_list')
def listing_all_applicants():
    administrator_data.listing_all_applicants()
    table_header = administrator_data.tags
    table_content = administrator_data.query
    return render_template('list.html', header=table_header, content=table_content)

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0')
