from models import *
import csv
import os


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
            related_school = School.select().where(School.name=="Budapest").get()
            City.create(name=city, related_school=related_school)
        elif city in miskolc_cities:
            related_school = School.select().where(School.name=="Miskolc").get()
            City.create(name=city, related_school=related_school)
        elif city in krakow_cities:
            related_school = School.select().where(School.name=="Krakow").get()
            City.create(name=city, related_school=related_school)

def csv_reader(filename):
    current_file_path = os.path.dirname(os.path.abspath(__file__))
    filename = current_file_path + "/data/" + str(filename)
    table = []
    with open(filename, "r", encoding='utf-8') as f:
        csvfile = csv.reader(f, delimiter=';')
        next(csvfile)
        for line in csvfile:
            table.append(line)
        return table

def create_by_csv(school, mentor_table):
    for mentor in mentor_table:
        Mentor.create(nickname=mentor[5],
                      first_name=mentor[0],
                      last_name=mentor[1],
                      year_of_birth=datetime.datetime.strptime(
                          mentor[2], '%Y%m%d'),
                      gender=mentor[3],
                      codecool_class=school)


create_dummy_schools(["Budapest", "Miskolc", "Krakow"])

create_dummy_city(["Budapest", "Székesfehérvár", "Tata", "Miskolc", "Eger", "Tokaj", "Krakow", "Warsaw", "Katovice"])
