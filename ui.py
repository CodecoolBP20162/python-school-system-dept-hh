from new_applicants import Newapplicants
from mentors import Mentors
from administrator import Administrator
import os

class Ui:

    @staticmethod
    def interface():

        while True:

            print("\nWelcome to Codecool School System:\n")
            print('''Chose a role:\n1. Applicant\n2. Mentor\n3. Administrator\n0. Quit\n''')

            choose = input("Please choose a role:")

            if choose == "1":
                Applicant_interface.applicant_menu()

            elif choose == "2":
                Mentor_interface.mentor_menu()


            elif choose == "3":
                Administrator_interface.administrator_menu()

            elif choose == "0":
                exit()

class Applicant_interface(Ui):

    @staticmethod
    def applicant_menu():

        print("Choose an option:\n")

        print("""1. New applicant registration\n2. Application details\n3. Interview details\n4. Questions\n0. Back to main menu\n""")

        app_menu_choice = input("Your choice:")

        if app_menu_choice == "1":
            Applicant_interface.new_applicant()

        elif app_menu_choice == "2":
            Applicant_interface.application_details()

        elif app_menu_choice == "3":
            Applicant_interface.interview_details()

        elif app_menu_choice == "4":
            Applicant_interface.questions()

        elif app_menu_choice == "0":
            Ui.interface()

    @staticmethod
    def new_applicant():

        collected_datas = Newapplicants.data_collection()
        new_applicant_datas = Newapplicants.new_applicant(
            collected_datas)

        if len(collected_datas) != 2:
            print("Your new application code: {code}\nDate of your interview:{date}".format(
                code=new_applicant_datas[0].code, date=new_applicant_datas[1].interviewslot.start))
            print("Please don't forget to save or write down your code!\n")

    @staticmethod
    def application_details():

        app_code_check = input("Your application code:")


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

    @staticmethod
    def interview_details():

        app_interview_check = input("Your application code:")


        try:

            app_datas = Newapplicants.check_applicant_interview(
                app_interview_check)

            print("Your interview starts at {date}".format(
                date=app_datas.start))

        except:
            print(
                "You don't have interview date yet. Please send an email(codecool@codlcode.com) and ask for a new date!")

    @staticmethod
    def questions():

        print(
            "1. Ask a question\n2. Question status\n0. Back to main menu")
        choose2 = input("Your choice:")
        if choose2 == "1":

            Newapplicants.add_question_to_database()

        elif choose2 == "2":

            table = Newapplicants.get_question_info()
            tablelist = ["Question", "Status", "Answer"]
            Administrator.prettytable(table, tablelist)

        elif choose2 == "0":
            Ui.interface()
        else:
            print("That is not a valid option!")

class Mentor_interface(Ui):

    @staticmethod
    def mentor_menu():

        print("Choose an option:\n")

        print("1. Interviews\n2. Questions\n0. Back to main menu\n")

        mentors_menu_choice = input("Your choice:")

        if mentors_menu_choice == "1":
            Mentor_interface.interviews()

        elif mentors_menu_choice == "2":
            Mentor_interface.questions()

        elif mentors_menu_choice == "0":
            Ui.interface()

    @staticmethod
    def interviews():

        mentor_id = input("Your ID:")

        Mentors.check_mentors_interviews(mentor_id)

    @staticmethod
    def questions():

        print("1. List questions\n2. Answer question (get the question ID ready!)\n0. Back to main menu\n")

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

        elif question_menu_choice == "0":
            Ui.interface()


class Administrator_interface(Ui):

    @staticmethod
    def administrator_menu():

        print("Choose an option:\n")

        print("1. Applicants\n2. Interviews\n3. Questions\n0. Back to main menu\n")

        admin_menu_choice = input("Your choice:")

        if admin_menu_choice == "1":
            Administrator_interface.applicant_menu()

        elif admin_menu_choice == "2":
            Administrator_interface.interviews()

        elif admin_menu_choice == "3":
            Administrator_interface.questions()

        elif admin_menu_choice == "0":
            Ui.interface()


    @staticmethod
    def applicant_menu():



        print("Choose an option:")

        print("""1. Applicants personal data\n2. Applicants filtered by...\n0. Back to main menu\n""")

        admin_app_menu_choice = input("Your choice:")

        if admin_app_menu_choice == "1":

            Administrator.applicants_personal_data()

        elif admin_app_menu_choice == "2":

            print("Choose a filter requirement:")

            print(
                """1. Applicants by status\n2. Applicants by interviews\n3. Applicants by location\n4. Applicants by city\n5. Interview with Mentor\n6. Applicant name and email by ID\n0. Back to main menu\n""")

            admin_filter_choice = input("Your choice:")

            if admin_filter_choice == "1":
                admin_subfilter_choice = input("Your choice(accepted/rejected/new/in progress:")
                Administrator.apps_by_status(admin_subfilter_choice)

            elif admin_filter_choice == "2":
                try:
                admin_filter = input("Please give a specific date in the following format:\n"
                                     "Example format: 2015-01-01 00:00: ")
                Administrator.apps_by_interview(admin_filter)
                except:
                    print("Date format is wrong!")

            elif admin_filter_choice == "3":

                admin_subfilter_choice = input("Write a school name:")
                Administrator.apps_by_location(admin_subfilter_choice)

            elif admin_filter_choice == "4":

                admin_subfilter_choice = input("Write a city name:")
                Administrator.apps_by_city(admin_subfilter_choice)


            elif admin_filter_choice == "5":

                admin_subfilter_choice = input("Write a name for mentor:")
                Administrator.apps_by_mentor(admin_subfilter_choice)

            elif admin_filter_choice == "6":
                admin_subfilter_choice = input("ApplicantID:")
                Administrator.emails_by_names(admin_subfilter_choice)

        elif admin_app_menu_choice == "0":
                Ui.interface()

    @staticmethod
    def interviews():


        print("Choose an option: ")

        print("""1. Listing all interviews\n2. Listing interviews filtered by...\n0.Back to main menu\n""")

        admin_interview_menu_choice = input("Your choice: ")

        if admin_interview_menu_choice == "1":

            Administrator.listing_all_interviews()

        elif admin_interview_menu_choice == "2":

            print("Choose a filter requirement: ")
            print(
                """1. Interviews by mentor\n2. Interviews by applicant code\n3. Interviews by school\n4. Interviews by date\n""")

            admin_filter_choice = input("Your choice:")
            if admin_filter_choice == "1":
                admin_filter = input("Please write mentor's name: ")
                Administrator.listing_interviews_by_mentor(admin_filter)
            elif admin_filter_choice == "2":
                admin_filter = input("Please write an applicant's code: ")
                Administrator.listing_interviews_by_applicant_code(admin_filter)
            elif admin_filter_choice == "3":
                admin_filter = input("Please give a School: ")
                Administrator.listing_interviews_by_school(admin_filter)
            elif admin_filter_choice == "4":
                try:
                    admin_filter = input("Please give a specific date in the following format:\n"
                                         "Example format: 2015-01-01 00:00: ")
                    Administrator.listing_interviews_by_date(admin_filter)
                except:
                    print("Date format is wrong!")
                    Administrator_interface.interviews()

        elif admin_interview_menu_choice == "0":
            Ui.interface()

    @staticmethod
    def questions():



        print(
            "1. Assign a mentor to answer a question (get mentor and question ID ready!)\n2. Listing questions filtered by...\n0. Back to main menu")

        admin_question_choice = input("Your choice:")

        if admin_question_choice == "1":
            Administrator.mentor_assigning()

        elif admin_question_choice == "2":

            print("Choose a filter requirement:")

            print(
                """1. Questions by status\n2. Questions by applicants\n3. Questions by school\n4. Questions by mentor\n6. Question by date\n""")

            question_filter_choice = input("Your choice:")

            if question_filter_choice == "1":
                admin_subfilter_choice = input("Your choice(answered/waiting for answer/new):")
                Administrator.question_by_status(admin_subfilter_choice)

            elif question_filter_choice == "2":
                admin_filter = input("Please write an application's name: ")
                Administrator.question_by_applicants(admin_filter)

            elif question_filter_choice == "3":
                admin_filter = input("Please give a School: ")
                Administrator.question_by_school(admin_filter)

            elif question_filter_choice == "4":
                admin_filter = input("Please write mentor's name: ")
                Administrator.question_by_mentor(admin_filter)

            elif question_filter_choice == "5":
                try:
                admin_filter = input("Please give a specific date in the following format:\n"
                                     "Example format: 2015-01-01 00:00: ")
                Administrator.question_by_date(admin_filter)
                except:
                    print("Date format is wrong!")

        elif admin_question_choice == "0":
            Ui.interface()
