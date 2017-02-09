from models import *
import csv
import os
from applicants import ApplicantsData
from datetime import datetime

class ExampleDataCreator:

    def csv_reader(self, filename):
        current_file_path = os.path.dirname(os.path.abspath(__file__))
        filename = current_file_path + "/example_csv_files/" + str(filename)
        table = []

        with open(filename, "r", encoding='utf-8') as f:
            csvfile = csv.reader(f, delimiter=';')
            next(csvfile)
            for line in csvfile:
                table.append(line)
            return table

    def create_dummy_schools(self, schools):
        for school in schools:
            School.create(name=school)

    def create_dummy_cities(self, cities):
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

    def create_dummy_mentors_by_csv(self, mentor_table):
        for mentor in mentor_table:
            school = School.select().where(School.name == mentor[1]).get()
            Mentor.create(name=mentor[0], related_school=school)

    def create_dummy_applicants_by_csv(self, applicants_table):
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
                             code=ApplicantsData.random_app_code(), school=related_school)

    def create_dummy_interview_slots_by_csv(self, interviewslot_table):
        for slot in interviewslot_table:
            mentor1 = Mentor.select().order_by(fn.Random()).limit(1)
            mentor1_obj = mentor1.get()
            mentor2 = Mentor.select().where((Mentor.name != mentor1_obj.name) & (Mentor.related_school == mentor1_obj.related_school)).order_by(fn.Random()).limit(1)
            InterviewSlot.create(start=datetime.strptime(slot[0], '%Y-%m-%d %H:%M'), end=datetime.strptime(slot[1], '%Y-%m-%d %H:%M'), reserved=False, mentor=mentor1, mentor2=mentor2)

    def build_tables(self, tables):
        db.connect()
        db.drop_tables(tables, safe=True, cascade=True)
        db.create_tables(tables, safe=True)
        