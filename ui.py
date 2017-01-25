import random
# from new_applicants import *


class Ui:

    @staticmethod
    def interface():

        app_inputs_list = []

        while True:

            print("\nWelcome to Codecool School System:\n")
            print('''Chose a role:\n
            1. Applicant
            2. Mentor
            3. Administrator
            4. Quit\n''')

            choose = str(input("Please choose a role:"))

            if choose == "1":
                name_input = str(input("Please enter your name:"))
                city_input = str(input("Please enter your city:"))
                print(name_input)
                app_inputs_list.append(name_input)
                app_inputs_list.append(city_input)


                return app_inputs_list

            elif choose == "2":
                pass

            elif choose == "3":
                pass

            elif choose == "0":
                exit()

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

#lajos = Ui.random_app_code()



Ui.interface()