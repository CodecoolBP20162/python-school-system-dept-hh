# This script can create the database tables based on your models

from models import *
from example_data import ExampleDataCreator



# List the tables here what you want to create...
data_creator=ExampleDataCreator()


data_creator.build_tables([School, City, Mentor, Applicant, InterviewSlot, Interview, Question, Answer])
data_creator.create_dummy_schools(["Budapest", "Miskolc", "Krakow"])
data_creator.create_dummy_cities(["Budapest", "Székesfehérvár", "Tata", "Miskolc",
                                  "Eger", "Tokaj", "Krakow", "Warsaw", "Katovice"])
data_creator.create_dummy_mentors_by_csv(data_creator.csv_reader("mentors.csv"))
data_creator.create_dummy_applicants_by_csv(data_creator.csv_reader("applicants.csv"))
data_creator.create_dummy_interview_slots_by_csv(data_creator.csv_reader("interviewslot.csv"))