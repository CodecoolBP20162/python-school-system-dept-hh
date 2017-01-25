from new_applicants import Newapplicants
import os

class Ui:

    @staticmethod
    def interface():


        while True:

            print("\nWelcome to Codecool School System:\n")
            print('''Chose a role:\n
            1. Applicant
            2. Mentor
            3. Administrator
            0. Quit\n''')

            choose = input("Please choose a role:")

            if choose == "1":
                print("Choose an option:\n")

                print("1. New applicant registration\n2. Application details:\n")

                app_menu_choice = input("Your choice:")

                if app_menu_choice == "1":
                    collected_datas = Newapplicants.data_collection()
                    new_applicant_datas = Newapplicants.new_applicant(collected_datas)

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print("Your new application code: {0}\nDate of your interview:XXXX".format(new_applicant_datas.code))
                    print("Please don't forget to save or write down your code!\n")


                elif app_menu_choice == "2":
                    app_code_check = input("Your application code:")

                    os.system('cls' if os.name == 'nt' else 'clear')

                    try:
                        app_datas = Newapplicants.check_applicant(app_code_check)
                        print("""\nYour registered data:
                        Status: {_0}
                        City: {_1}
                        Code: {_2}
                        School: {_3}\n""".format(_0=app_datas.status,_1=app_datas.city.name,_2=app_datas.code,_3=app_datas.school.name))
                    except:
                        print("You did not register yet or your code is wrong!\n")

            elif choose == "2":
                pass

            elif choose == "3":
                pass

            elif choose == "0":
                exit()



