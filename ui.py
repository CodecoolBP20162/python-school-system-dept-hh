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

                print("1. Interviews\n2. Questions")

                mentors_menu_choice = input("Your choice:")

                if mentors_menu_choice == "1":
                    mentor_id = input("Your ID:")

                    os.system('cls' if os.name == 'nt' else 'clear')


                    Mentors.check_mentors_interviews(mentor_id)

                elif mentors_menu_choice == "2":
                    print("1. List questions\n2. Answer question (get the question ID ready!)")

                    question_menu_choice = input("Your choice:")

                    if question_menu_choice == "1":

                        table = Mentors.question_displayer()
                        for row in table:
                            print("\nSubmission date:")
                            print("\t{date}".format(date=row[0]))
                            print("Question:")
                            print("\t{question}".format(question=row[1]))
                            print("Application code:")
                            print("\t{code}".format(code=row[2]))
                            print("ID:")
                            print("\t{code}".format(code=row[3]))
                        print()

                    elif question_menu_choice == "2":

                        Mentors.question_answering()




            elif choose == "3":
                print("Choose an option:\n")

                print("1. Applicants\n2.Interviews")

                admin_menu_choice = input("Your choice:")

                if admin_menu_choice == "1":
                    #mentor_id = input("Your ID:") -----> space for admin identity check

                    os.system('cls' if os.name == 'nt' else 'clear')


                    print("Choose an option:")

                    print("""1.Applicants personal data\n2.Applicants filtered by...""")

                    admin_app_menu_choice = input("Your choice:")

                    if admin_app_menu_choice == "1":

                        Administrator.applicants_personal_data()

                    elif admin_app_menu_choice == "2":

                        print("Choose a filter requirement:")
                        print("""1.Applicants by status Status\n2.Applicants by interviews\n3.Applicants by location\n4.Applicants by city\n5.Interview with Mentor""")
                        admin_filter_choice = input("Your choice:")

                        if admin_filter_choice == "1":
                            admin_subfilter_choice = input("Your choice(accepted/rejected/new/in progress:")
                            Administrator.apps_by_status(admin_subfilter_choice)

                        elif admin_filter_choice == "2":
                            Administrator.apps_by_interview()

                        elif admin_filter_choice == "3":
                            try:
                                admin_subfilter_choice = input("Write a school name:")
                                Administrator.apps_by_location(admin_subfilter_choice)
                            except TypeError:
                                print("There isn't any school with this name in the database.")
                        elif admin_filter_choice == "4":
                            try:
                                admin_subfilter_choice = input("Write a city name:")
                                Administrator.apps_by_city(admin_subfilter_choice)
                            except TypeError:
                                print("There isn't any city with this name in the database.")

                        elif admin_filter_choice == "5":
                            try:
                                admin_subfilter_choice = input("Write a name for mentor:")
                                Administrator.apps_by_mentor(admin_subfilter_choice)
                            except TypeError:
                                print("There isn't any mentor with this name in the database.")




                if admin_menu_choice == "2":
                    #mentor_id = input("Your ID:") -----> space for admin identity check

                    os.system('cls' if os.name == 'nt' else 'clear')








            elif choose == "0":
                exit()
