from models import *
import csv
import os
from applicants import ApplicantsData
from datetime import datetime


class ExampleDataCreator:

    @staticmethod
    def csv_reader(filename):
        current_file_path = os.path.dirname(os.path.abspath(__file__))
        filename = current_file_path + "/example_csv_files/" + str(filename)
        table = []

        with open(filename, "r", encoding='utf-8') as f:
            csvfile = csv.reader(f, delimiter=';')
            next(csvfile)
            for line in csvfile:
                table.append(line)
            return table

    @staticmethod
    def create_dummy_schools(schools):
        for school in schools:
            School.create(name=school)

    @staticmethod
    def create_dummy_cities(cities):
        budapest_cities = ["Budapest", "Székesfehérvár", "Tata"]
        miskolc_cities = ["Miskolc", "Eger", "Tokaj"]
        krakow_cities = ["Krakow", "Warsaw", "Katovice"]

        for city in cities:
            if city in budapest_cities:
                related_school = School.select().where(School.name == "Budapest").get()
                City.create(name=city, related_school=related_school)
            elif city in miskolc_cities:
                related_school = School.select().where(School.name == "Miskolc").get()
                City.create(name=city, related_school=related_school)
            elif city in krakow_cities:
                related_school = School.select().where(School.name == "Krakow").get()
                City.create(name=city, related_school=related_school)

    @staticmethod
    def create_dummy_mentors_by_csv(mentor_table):
        for mentor in mentor_table:
            school = School.select().where(School.name == mentor[2]).get()
            Mentor.create(name=mentor[0], email=mentor[
                          1], password=ApplicantsData.random_app_code("mentor"), related_school=school)

    @staticmethod
    def create_dummy_applicants_by_csv(applicants_table):
        budapest_cities = ["Budapest", "Székesfehérvár", "Tata"]
        miskolc_cities = ["Miskolc", "Eger", "Tokaj"]
        krakow_cities = ["Krakow", "Warsaw", "Katovice"]

        for applicant in applicants_table:
            applicant_city = City.select().where(
                City.name == applicant[1]).get()
            related_school = ""
            if applicant[1] in budapest_cities:
                related_school = School.select().where(School.name == "Budapest").get()
            elif applicant[1] in miskolc_cities:
                related_school = School.select().where(School.name == "Miskolc").get()
            elif applicant[1] in krakow_cities:
                related_school = School.select().where(School.name == "Krakow").get()

            Applicant.create(name=applicant[0], city=applicant_city, email=applicant[2], status=applicant[3],
                             code=ApplicantsData.random_app_code("applicant"), school=related_school)

    @staticmethod
    def create_dummy_admins():
        name_list = ["Dénes", "Eszti", "Petya", "Tomi", "admin"]
        email_list = ["codecool.depth+szdenes@gmail.com", "codecool.depth+leszter@gmail.com",
                      "codecool.depth+szpeter@gmail.com", "codecool.depth+vtamas@gmail.com", "codecool.depth+admin@gmail.com"]
        password_list = ["1234", "5678", "9111", "1213", "admin"]

        for x in range(len(name_list)):
            Admin.create(name=name_list[x], password=password_list[
                         x], email=email_list[x])

    @staticmethod
    def create_dummy_interview_slots_by_csv(interviewslot_table):
        for slot in interviewslot_table:
            mentor_select = Mentor.select().order_by(fn.Random()).limit(1)
            mentor1 = mentor_select.get()
            mentor2 = Mentor.select().where(
                (Mentor.name != mentor1.name) & (Mentor.related_school == mentor1.related_school)).get()
            InterviewSlot.create(start=datetime.strptime(slot[0], '%Y-%m-%d %H:%M'),
                                 end=datetime.strptime(slot[1], '%Y-%m-%d %H:%M'), reserved=False, mentor=mentor1,
                                 mentor2=mentor2)

    @staticmethod
    def create_user_login_data():
        applicants = Applicant.select()
        mentors = Mentor.select()
        admins = Admin.select()
        for applicant in applicants:
            User.create(email=applicant.email, password=applicant.code,
                        user_status=applicant.user_status)
        for mentor in mentors:
            User.create(email=mentor.email, password=mentor.password,
                        user_status=mentor.user_status)
        for admin in admins:
            User.create(email=admin.email, password=admin.password,
                        user_status=admin.user_status)

    @staticmethod
    def build_tables(tables):
        db.connect()
        db.drop_tables(tables, safe=True, cascade=True)
        db.create_tables(tables, safe=True)
