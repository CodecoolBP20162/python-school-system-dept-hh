from models import *
from example_data import ExampleDataCreator


class Builder:
    def __init__(self):
        self.data_creator = ExampleDataCreator()

    def create_tables_and_dummy_data(self):
        self.data_creator.build_tables(
            [School, City, Mentor, Applicant, InterviewSlot, Interview, Question, Answer, Email])
        self.data_creator.create_dummy_schools(["Budapest", "Miskolc", "Krakow"])
        self.data_creator.create_dummy_cities(["Budapest", "Székesfehérvár", "Tata", "Miskolc",
                                               "Eger", "Tokaj", "Krakow", "Warsaw", "Katovice"])
        self.data_creator.create_dummy_mentors_by_csv(self.data_creator.csv_reader("mentors.csv"))
        self.data_creator.create_dummy_applicants_by_csv(self.data_creator.csv_reader("applicants.csv"))
        self.data_creator.create_dummy_interview_slots_by_csv(self.data_creator.csv_reader("interviewslot.csv"))


Builder().create_tables_and_dummy_data()
