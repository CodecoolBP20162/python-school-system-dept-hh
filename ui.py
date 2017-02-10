from administrator import AdministratorData
from prettytable import PrettyTable
from mentors import MentorsData
from applicants import ApplicantsData


class Menu:
    def __init__(self):
        self.header = None
        self.options = None
        self.exit_message = None
        self.table = PrettyTable(None, None)
        self.administrator_data = AdministratorData()
        self.applicants_data = ApplicantsData()
        self.mentors_data = MentorsData()

    def print_menu(self):
        print(self.header + ":")
        x = 1
        for option in self.options:
            print("(" + str(x) + ") " + option)
            x += 1
        print("(0) " + self.exit_message)

    def main_menu(self):
        while True:
            self.header = "Main menu"
            self.options = ["Applicant menu",
                            "Mentor menu", "Administrator menu"]
            self.exit_message = "Exit"
            self.print_menu()

            user_input = input("Please choose a role: ")

            if user_input == "1":
                self.applicant_menu()
            elif user_input == "2":
                self.mentor_menu()
            elif user_input == "3":
                self.admin_menu()
            elif user_input == "0":
                exit()
            else:
                print("Wrong input")

    def applicant_menu(self):
        while True:
            self.header = "Applicant menu"
            self.options = ["New applicant registration",
                            "Application details", "Interview details", "Questions"]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option: ")

            if user_input == "1":
                city_input = input("Please give your city: ")
                name_input = input("Please give your name: ")
                email_input = input("Please give your email adress: ")
                try:
                    self.applicants_data.new_applicant(city_input, name_input, email_input)
                    print("You have successfully applied.")
                except:
                    print("Something went wrong! Please try again.")
            elif user_input == "2":
                user_input = input("Please give your application code: ")
                self.applicants_data.check_applicant(user_input)
                self.table = PrettyTable(
                    self.applicants_data.results, self.applicants_data.tags)
                self.table.draw_table()
            elif user_input == "3":
                user_input = input("Please give your application code: ")
                self.applicants_data.check_applicant_interview(user_input)
                self.table = PrettyTable(
                    self.applicants_data.results, self.applicants_data.tags)
                self.table.draw_table()
            elif user_input == "4":
                self.applicant_question_menu()
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def applicant_question_menu(self):
        while True:
            self.header = "Question menu"
            self.options = ["Ask a question",
                            "Question status"]

            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option: ")

            if user_input == "1":
                code_input = input("Please give your application code: ")
                question_input = input("Please give your question: ")
                try:
                    self.applicants_data.add_question_to_database(code_input, question_input)
                    print("Your question is successfully added.")
                except:
                    print("Something went wrong! Please try again.")
            elif user_input == "2":
                user_input = input("Please give your application code: ")
                self.applicants_data.get_question_info(user_input)
                self.table = PrettyTable(
                    self.applicants_data.results, self.applicants_data.tags)
                self.table.draw_table()
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def mentor_menu(self):
        while True:
            self.header = "Mentor menu"
            self.options = ["Interviews", "Questions"]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option: ")

            if user_input == "1":
                user_input = input("Please give your ID: ")
                self.mentors_data.mentors_interviews_data(user_input)
                self.table = PrettyTable(
                    self.mentors_data.results, self.mentors_data.tags)
                self.table.draw_table()
            elif user_input == "2":
                self.mentor_questions_menu()
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def mentor_questions_menu(self):
        while True:
            self.header = "Question menu"
            self.options = ["List questions",
                            "Answer question (get the question ID ready!)"]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option: ")

            if user_input == "1":
                user_input = input("Please give your ID: ")
                self.mentors_data.question_data(user_input)
                self.table = PrettyTable(
                    self.mentors_data.results, self.mentors_data.tags)
                self.table.draw_table()
            elif user_input == "2":
                question = input("Please give the question ID: ")
                answer = input("Please type your answer: ")
                try:
                    self.mentors_data.question_answering(question, answer)
                    print("Your answer is successfully submitted.")
                except:
                    print("Something went wrong! Please try again.")

            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def admin_menu(self):
        while True:
            self.header = "Administrator menu"
            self.options = ["Applicants", "Interviews",
                            "Questions"]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option: ")

            if user_input == "1":
                self.admin_applicant_menu()
            elif user_input == "2":
                self.admin_interviews_menu()
            elif user_input == "3":
                self.admin_questions_menu()
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def admin_applicant_menu(self):
        while True:
            self.header = "Applicants menu"
            self.options = ["Listing all applicants",
                            "Applicants filtered by..."]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option: ")

            if user_input == "1":
                self.administrator_data.listing_all_applicants()
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "2":
                self.admin_applicant_filter_menu()
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def admin_applicant_filter_menu(self):
        while True:
            self.header = "Filter applicants by:"
            self.options = ["Status", "Interviews",
                            "Location", "City", "Interview with Mentor", "Applicant code"]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option: ")

            if user_input == "1":
                user_input = input(
                    "Your choice(accepted/rejected/new/in progress): ")
                self.administrator_data.applicants_by_status(user_input)
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "2":
                user_input = input("Please give a specific date in the following format:\n"
                                   "Example format: 2015-01-01: ")
                try:
                    self.administrator_data.applicants_by_interview(user_input)
                except ValueError:
                    print("Date is not in the right format!")
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "3":
                user_input = input("Please give a location: ")
                self.administrator_data.applicants_by_location(user_input)
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "4":
                user_input = input("Please give a city: ")
                self.administrator_data.applicants_by_city(user_input)
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "5":
                user_input = input("Please give a mentor's name: ")
                self.administrator_data.applicants_by_mentor(user_input)
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "6":
                user_input = input("Please give an application code: ")
                self.administrator_data.applicant_email_by_applicant_code(
                    user_input)
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def admin_interviews_menu(self):
        while True:
            self.header = "Interview menu"
            self.options = ["Listing all interviews",
                            "Listing interviews filtered by..."]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option:")

            if user_input == "1":
                self.administrator_data.listing_all_interviews()
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "2":
                self.admin_interview_filter_menu()
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def admin_interviews_filter_menu(self):
        while True:
            self.header = "Filter interviews by..."

    def admin_interview_filter_menu(self):
        while True:
            self.header = "Filter interviews by"
            self.options = ["Mentor", "Applicant code", "School", "Date"]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option:")

            if user_input == "1":
                user_input = input("Please give a mentor's name: ")
                self.administrator_data.listing_interviews_by_mentor(user_input)
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "2":
                user_input = input("Please give an application code: ")
                self.administrator_data.listing_interviews_by_applicant_code(
                    user_input)
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "3":
                user_input = input("Please give a school location: ")
                self.administrator_data.listing_interviews_by_school(
                    user_input)
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "4":
                user_input = input("Please give a specific date in the following format:\n"
                                   "Example format: 2015-01-01: ")
                try:
                    self.administrator_data.listing_interviews_by_date(
                        user_input)
                except ValueError:
                    print("Date is not in the right format!")
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def admin_questions_menu(self):
        while True:
            self.header = "Questions menu"
            self.options = [
                "Assign a mentor to answer a question (get mentor and question ID ready!)",
                "List questions filtered by..."]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option:")

            if user_input == "1":
                mentor_id = input("Please give a mentor's ID: ")
                question_id = input("Please give a question's ID:")
                try:
                    self.administrator_data.assign_mentor_to_question(mentor_id, question_id)
                    print("The question is given to the mentor.")
                except:
                    print("Something went wrong! Please try again.")
            elif user_input == "2":
                self.admin_question_filter_menu()
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def admin_question_filter_menu(self):
        while True:
            self.header = "Filter questions by"
            self.options = ["Status", "Applicants", "School", "Mentor", "Date"]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option: ")

            if user_input == "1":
                user_input = input("Your choice(answered/waiting for answer/new): ")
                self.administrator_data.question_by_status(user_input)
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "2":
                user_input = input("Please give an application code: ")
                self.administrator_data.question_by_applicants(user_input)
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "3":
                user_input = input("Please give a school: ")
                self.administrator_data.question_by_school(user_input)
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "4":
                user_input = input("Please give a mentor's name: ")
                self.administrator_data.question_by_mentor(user_input)
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "5":
                user_input = input("Please give a specific date in the following format:\n"
                                   "Example format: 2015-01-01: ")
                try:
                    self.administrator_data.question_by_date(user_input)
                except ValueError:
                    print("Date is not in the right format!")
                self.table = PrettyTable(
                    self.administrator_data.results, self.administrator_data.tags)
                self.table.draw_table()
            elif user_input == "0":
                return
            else:
                print("Wrong input")
