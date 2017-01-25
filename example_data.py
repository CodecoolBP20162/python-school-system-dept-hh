from models import *
import csv
import os
from new_applicants import Newapplicants
from datetime import datetime


# This script can generate example data for "City" and "InterviewSlot" models.

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


def create_dummy_schools(schools):
    for school in schools:
        School.create(name=school)


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


def create_dummy_mentors_by_csv(mentor_table):
    for mentor in mentor_table:
        school = School.select().where(School.name == mentor[1]).get()
        Mentor.create(name=mentor[0], related_school=school)


def create_dummy_applicants_by_csv(applicants_table):
    budapest_cities = ["Budapest", "Székesfehérvár", "Tata"]
    miskolc_cities = ["Miskolc", "Eger", "Tokaj"]
    krakow_cities = ["Krakow", "Warsaw", "Katovice"]

    for applicant in applicants_table:
        applicant_city = City.select().where(City.name == applicant[1]).get()
        related_school = ""
        if applicant[1] in budapest_cities:
            related_school = School.select().where(School.name == "Budapest").get()
        elif applicant[1] in miskolc_cities:
            related_school = School.select().where(School.name == "Miskolc").get()
        elif applicant[1] in krakow_cities:
            related_school = School.select().where(School.name == "Krakow").get()

        Applicant.create(name=applicant[0], city=applicant_city, status=applicant[2],
                         code=Newapplicants.random_app_code(), school=related_school)


def create_dummy_interview_slots_by_csv(interviewslot_table):
    for slot in interviewslot_table:
        mentors = Mentor.select().order_by(fn.Random()).limit(1)
        InterviewSlot.create(start=datetime.strptime(slot[0], '%Y-%m-%d %H:%M'), end=datetime.strptime(
            slot[1], '%Y-%m-%d %H:%M'), reserved=False, mentor=mentors)
