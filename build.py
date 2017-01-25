# This script can create the database tables based on your models

from models import *
import example_data

db.connect()
# List the tables here what you want to create...

def build_tables(tables):
    for table in tables:
        if table.table_exists():
            table.drop_table(fail_silently=True, cascade=True)
    db.create_tables(tables, safe=True)

build_tables([School, City, Mentor, Applicant, InterviewSlot, Interview])

example_data.create_dummy_schools(["Budapest", "Miskolc", "Krakow"])

example_data.create_dummy_city(["Budapest", "Székesfehérvár", "Tata", "Miskolc",
                   "Eger", "Tokaj", "Krakow", "Warsaw", "Katovice"])

example_data.create_mentor_by_csv(example_data.csv_reader("mentors.csv"))

