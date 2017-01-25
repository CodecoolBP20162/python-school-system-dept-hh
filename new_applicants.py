# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!
import random
from models import *



class Newapplicants:

    @staticmethod
    def check_applicant(code_input):

        app_datas = Applicant.select().where(Applicant.code == code_input).get()

        return app_datas

    @staticmethod
    def data_collection():
        app_inputs_list = []
        app_inputs_list.append(str(input("Please enter your name:")))
        app_inputs_list.append(str(input("Please enter your city:")))
        return app_inputs_list


    @staticmethod
    def new_applicant(app_data_list):
        budapest_cities = ["Budapest", "Székesfehérvár", "Tata"]
        miskolc_cities = ["Miskolc", "Eger", "Tokaj"]
        krakow_cities = ["Krakow", "Warsaw", "Katovice"]
        related_school = ""
        new_applicant_city = City.select().where(City.name == app_data_list[1]).get()

        if app_data_list[1] in budapest_cities:
            related_school = School.select().where(School.name == "Budapest").get()
        elif app_data_list[1] in miskolc_cities:
            related_school = School.select().where(School.name == "Miskolc").get()
        elif app_data_list[1] in krakow_cities:
            related_school = School.select().where(School.name == "Krakow").get()


        new_applicant = Applicant.create(name=app_data_list[0], city=new_applicant_city, school = related_school, status="new",
                         code=Newapplicants.random_app_code())

        return new_applicant


    @staticmethod
    def random_app_code():
        symbols = "#$%&'()*+,-./?@^_`{|}~"
        digits = "0123456789"
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        charlist = []
        charlist.append((random.sample(lowercase, 2)) +
                        (random.sample(uppercase, 2)) +
                        (random.sample(digits, 2)) +
                        (random.sample(symbols, 2)))

        random.shuffle(charlist[0])
        rand_code = "".join(charlist[0])

        code_table = Applicant.select(Applicant.code)

        #ANOTHER THECNIC
        # code_table = Applicant.select(Applicant.code).where(Applicant.code = rand_code)
        #   if code_table = None:
        #       generate_random()

        for code in code_table:
            if rand_code == code:
                generate_random()

        return rand_code
