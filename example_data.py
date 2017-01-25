from models import *
import csv
import os
from new_applicants import Newapplicants


# This script can generate example data for "City" and "InterviewSlot" models.

def create_dummy_schools(schools):
    for school in schools:
        School.create(name=school)


def create_dummy_city(cities):
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


def create_dummy_mentor_by_csv(mentor_table):
    for mentor in mentor_table:
        school = School.select().where(School.name == mentor[1]).get()
        Mentor.create(name=mentor[0], related_school=school)


def create_dummy_applicants_by_csv(applicants_table):
    for applicant in applicants_table:
        applicant_city = City.select().where(City.name == applicant[1]).get()
        Applicant.create(name=applicant[0], city=applicant_city, status=applicant[2],
                         code=Newapplicants.random_app_code())
