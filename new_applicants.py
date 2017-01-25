# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!
import random
from models import *
import ui


class Newapplicants:
    @staticmethod
    def new_applicant(app_data_list):
        new_applicant_city = City.select().where(City.name == app_data_list[1]).get()
        Applicant.create(name=app_data_list[0], city=new_applicant_city, status="new",
                         code=Newapplicants.random_app_code())

    # -------------------> Tomi make a city-school relation method
    @staticmethod
    def random_app_code():  # ----------argument will be the app_table
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

        # ANOTHER THECNIC
        # code_table = Applicant.select(Applicant.code).where(Applicant.code = rand_code)
        #   if code_table = None:
        #       generate_random()

        for code in code_table:
            if rand_code == code:
                generate_random()

        return rand_code
