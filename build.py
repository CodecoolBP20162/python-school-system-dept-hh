# This script can create the database tables based on your models

from models import *
import example_data

db.connect()

'''
SELECT city.name, school.name
FROM applicant
LEFT JOIN city ON applicant.city_id = city.id
LEFT JOIN school ON applicant.school_id = school.id;
'''

query = Applicant.select()
for query_item in query:
    print(query_item.city.name, query_item.school.name)

'''
# List the tables here what you want to create...

def build_tables(tables):
    db.drop_tables(tables,safe=True,cascade=True)
    db.create_tables(tables, safe=True)


build_tables([School, City, Mentor, Applicant, InterviewSlot, Interview, Question, Answer])

example_data.create_dummy_schools(["Budapest", "Miskolc", "Krakow"])

example_data.create_dummy_cities(["Budapest", "Székesfehérvár", "Tata", "Miskolc",
                                  "Eger", "Tokaj", "Krakow", "Warsaw", "Katovice"])

example_data.create_dummy_mentors_by_csv(example_data.csv_reader("mentors.csv"))

example_data.create_dummy_applicants_by_csv(example_data.csv_reader("applicants.csv"))

example_data.create_dummy_interview_slots_by_csv(example_data.csv_reader("interviewslot.csv"))
'''