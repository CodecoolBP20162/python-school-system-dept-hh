from administrator import AdministratorData
from prettytable import PrettyTable
from mentors import MentorsData
from new_applicants import ApplicantsData


class Menu:
    def __init__(self):
        self.header = None
        self.options = None
        self.exit_message = None
        self.admin = AdministratorData()
        self.table = PrettyTable(None, None)
        self.administrator = AdministratorData()

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
                            "Mentor menu", "Adminsitrator menu"]
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
                break
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
                print("something")
            elif user_input == "2":
                print("something")
            elif user_input == "3":
                print("something")
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
                print("something")
            elif user_input == "2":
                print("something")
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
                print("something")
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
                print("something")
            elif user_input == "2":
                print("something")
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
                self.administrator.listing_all_applicants()
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
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
                self.administrator.applicants_by_status(user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "2":
                user_input = input("Please give a specific date in the following format:\n"
                                   "Example format: 2015-01-01: ")
                self.administrator.applicants_by_interview(user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "3":
                user_input = input("Please give a location: ")
                self.administrator.applicants_by_location(user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "4":
                user_input = input("Please give a city: ")
                self.administrator.applicants_by_city(user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "5":
                user_input = input("Please give a mentor: ")
                self.administrator.applicants_by_mentor(user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "6":
                user_input = input("Please give an application code: ")
                self.administrator.applicant_email_by_applicant_code(
                    user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
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
                self.administrator.listing_all_interviews()
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
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
                user_input = input("Please give a mentor: ")
                self.administrator.listing_interviews_by_mentor(user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "2":
                user_input = input("Please give an application code: ")
                self.administrator.listing_interviews_by_applicant_code(
                    user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "3":
                user_input = input("Please give a school: ")
                self.administrator.listing_interviews_by_school(
                    user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "4":
                user_input = input("Please give a specific date in the following format:\n"
                                   "Example format: 2015-01-01: ")
                self.administrator.listing_interviews_by_date(
                    user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
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
                    self.admin.assign_mentor_to_question(mentor_id, question_id)
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
                self.administrator.question_by_status(user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "2":
                user_input = input("Please give an applicant: ")
                self.administrator.question_by_applicants(user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "3":
                user_input = input("Please give a school: ")
                self.administrator.question_by_school(user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "4":
                user_input = input("Please give a mentor: ")
                self.administrator.question_by_mentor(user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "5":
                user_input = input("Please give a specific date in the following format:\n"
                                   "Example format: 2015-01-01: ")
                self.administrator.question_by_date(user_input)
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def interface_flow(self):
        self.main_menu()


ui = Menu()
ui.interface_flow()
