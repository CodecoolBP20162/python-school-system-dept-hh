# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!

from models import *

@staticmethod
def new_applicant(app_data_list):
    Applicant.create(name = app_data_list[1], city = "Kecskemét", status = "NEW", code = ui.random_app_code())

@staticmethod
def random_app_code():  #----------argument will be the app_table
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


#CHECK EQUAL CODE OCCURENCE
    #for  in range(len(app_table)):
     #   if generated == app_table[something]:
      #     generate_random() --->again

    return rand_code