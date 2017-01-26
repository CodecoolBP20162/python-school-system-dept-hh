from new_applicants import Newapplicants
from mentors import Mentors
from administrator import Administrator
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

                print(
                    "1. New applicant registration\n2. Application details\n3. Interview details\n4. Questions")

                app_menu_choice = input("Your choice:")

                if app_menu_choice == "1":
                    collected_datas = Newapplicants.data_collection()
                    new_applicant_datas = Newapplicants.new_applicant(
                        collected_datas)

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print("Your new application code: {code}\nDate of your interview:{date}".format(
                        code=new_applicant_datas[0].code, date=new_applicant_datas[1].interviewslot.start))
                    print("Please don't forget to save or write down your code!\n")

                elif app_menu_choice == "2":
                    app_code_check = input("Your application code:")

                    os.system('cls' if os.name == 'nt' else 'clear')

                    try:
                        app_datas = Newapplicants.check_applicant(
                            app_code_check)
                        print("""\nYour registered data:
                        Status: {_0}
                        City: {_1}
                        Code: {_2}
                        School: {_3}\n""".format(_0=app_datas.status, _1=app_datas.city.name, _2=app_datas.code,
                                                 _3=app_datas.school.name))
                    except:
                        print("You did not register yet or your code is wrong!\n")

                elif app_menu_choice == "3":
                    app_interview_check = input("Your application code:")

                    os.system('cls' if os.name == 'nt' else 'clear')

                    try:

                        app_datas = Newapplicants.check_applicant_interview(
                            app_interview_check)

                        print("Your interview starts at {date}".format(
                            date=app_datas.start))

                    except:
                        print(
                            "You don't have interview date yet. Please send an email(codecool@codlcode.com) and ask for a new date!")

                elif app_menu_choice == "4":
                    print(
                        "\n1. Ask a question\n2. Question status\n3. Back to main menu")
                    choose2 = input("Your choice:")
                    if choose2 == "1":

                        Newapplicants.add_question_to_database()

                    elif choose2 == "2":

                        table = Newapplicants.get_question_info()
                        tablelist = ["Question", "Status", "Answer"]
                        Administrator.prettytable(table, tablelist)

                    elif choose2 == "3":
                        pass
                    else:
                        print("That is not a valid option!")

            elif choose == "2":
                print("Choose an option:\n")

                print("1. Interviews\n")

                mentors_menu_choice = input("Your choice:")

                if mentors_menu_choice == "1":
                    mentor_id = input("Your ID:")

                    os.system('cls' if os.name == 'nt' else 'clear')


                    Mentors.check_mentors_interviews(mentor_id)



            elif choose == "3":
                print("Choose an option:\n")

                print("1. Applicants\n2.Interviews")

                admin_menu_choice = input("Your choice:")

                if admin_menu_choice == "1":
                    #mentor_id = input("Your ID:") -----> space for admin identity check

                    os.system('cls' if os.name == 'nt' else 'clear')


                    print("Choose an option:")

                    print("""1.Aplicants personal data""")

                    admin_app_menu_choice = input("Your choice:")

                    if admin_app_menu_choice == "1":
                        Administrator.applicants_personal_data()


                if admin_menu_choice == "2":
                    #mentor_id = input("Your ID:") -----> space for admin identity check

                    os.system('cls' if os.name == 'nt' else 'clear')








            elif choose == "0":
                exit()
