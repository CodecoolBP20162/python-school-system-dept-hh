from models import *


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


create_dummy_schools(["Budapest", "Miskolc", "Krakow"])

create_dummy_city(["Budapest", "Székesfehérvár", "Tata", "Miskolc", "Eger", "Tokaj", "Krakow", "Warsaw", "Katovice"])
