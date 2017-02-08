from administrator import AdministratorData
<<<<<<< Updated upstream


=======
from prettytable import PrettyTable
>>>>>>> Stashed changes
# from mentor import MentorData
# from applicants import ApplicantData


class Menu:
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
    def __init__(self):
        self.header = None
        self.options = None
        self.exit_message = None
<<<<<<< Updated upstream
        self.admin = AdministratorData()
=======
        self.table = PrettyTable(None, None)
        self.administrator = AdministratorData()
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
                            "Mentor menu", "Adminsitrator menu"]
=======
                            "Mentor menu", "Administrator menu"]
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
            self.header = "Questions menu"
            self.options = ["Ask a question", "Question status"]
=======
            self.header = "Question menu"
            self.options = ["Ask a question",
                            "Question status"]
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                self.mentor_question_menu()
=======
                self.mentor_questions_menu()
>>>>>>> Stashed changes
            elif user_input == "0":
                return
            else:
                print("Wrong input")

<<<<<<< Updated upstream
    def mentor_question_menu(self):
        while True:
            self.header = "Questions menu"
            self.options = ["List questions","Answer question (get the question ID ready!)"]
=======
    def mentor_questions_menu(self):
        while True:
            self.header = "Question menu"
            self.options = ["List questions",
                            "Answer question (get the question ID ready!)"]
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                self.admin_applicants_menu()
=======
                self.admin_applicant_menu()
>>>>>>> Stashed changes
            elif user_input == "2":
                self.admin_interviews_menu()
            elif user_input == "3":
                self.admin_questions_menu()
            elif user_input == "0":
                return
            else:
                print("Wrong input")

<<<<<<< Updated upstream
    def admin_applicants_menu(self):
        while True:
            self.header = "Applicant menu"
=======
    def admin_applicant_menu(self):
        while True:
            self.header = "Applicants menu"
>>>>>>> Stashed changes
            self.options = ["Listing all applicants",
                            "Applicants filtered by..."]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option: ")

            if user_input == "1":
<<<<<<< Updated upstream
                print("something")
            elif user_input == "2":
                self.admin_applicants_filter_menu()
=======
                self.administrator.applicants_personal_data()
                self.table = PrettyTable(
                    self.administrator.results, self.administrator.tags)
                self.table.draw_table()
            elif user_input == "2":
                self.admin_applicant_filter_menu()
>>>>>>> Stashed changes
            elif user_input == "0":
                return
            else:
                print("Wrong input")

<<<<<<< Updated upstream
    def admin_applicants_filter_menu(self):
        while True:
            self.header = "Filter applicants by..."
            self.options = ["Status", "Interviews", "Location", "City", "Interview with Mentor", "Code"]
=======
    def admin_applicant_filter_menu(self):
        while True:
            self.header = "Filter applicants by:"
            self.options = ["Status", "Interviews",
                            "Location", "City", "Interview with Mentor", "Applicant code"]
>>>>>>> Stashed changes
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option: ")

            if user_input == "1":
<<<<<<< Updated upstream
                print("something")
            elif user_input == "2":
                print("something")
            elif user_input == "3":
                print("something")
            elif user_input == "4":
                print("something")
            elif user_input == "5":
                print("something")
            elif user_input == "6":
                print("something")
=======
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
>>>>>>> Stashed changes
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def admin_interviews_menu(self):
        while True:
<<<<<<< Updated upstream
            self.header = "Applicant menu"
            self.options = ["Listing all interviews", "Listing interviews filtered by..."]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option: ")

            if user_input == "1":
                print("something")
            elif user_input == "2":
                self.admin_interviews_filter_menu()
=======
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
>>>>>>> Stashed changes
            elif user_input == "0":
                return
            else:
                print("Wrong input")

<<<<<<< Updated upstream
    def admin_interviews_filter_menu(self):
        while True:
            self.header = "Filter interviews by..."
=======
    def admin_interview_filter_menu(self):
        while True:
            self.header = "Filter interviews by"
>>>>>>> Stashed changes
            self.options = ["Mentor", "Applicant code", "School", "Date"]
            self.exit_message = "Back"
            self.print_menu()

<<<<<<< Updated upstream
            user_input = input("Please choose an option: ")

            if user_input == "1":
                print("something")
            elif user_input == "2":
                print("something")
            elif user_input == "3":
                print("something")
            elif user_input == "4":
                print("something")
=======
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
>>>>>>> Stashed changes
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def admin_questions_menu(self):
        while True:
            self.header = "Questions menu"
<<<<<<< Updated upstream
            self.options = ["Assign a mentor to answer a question (get mentor and question ID ready!)",
                            "Filter questions by..."]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option: ")

            if user_input == "1":
                print("something")
            elif user_input == "2":
                self.admin_questions_filter_menu()
=======
            self.options = [
                "Assign a mentor to answer a question (get mentor and question ID ready!)", "List questions filtered by..."]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option:")

            if user_input == "1":
                mentor_id = input("Please give a mentor's ID: ")
                question_id = input("Please give a question's ID:")
                try:
                    assign_mentor_to_question(mentor_id, question_id)
                except:
                    print("Something went wrong! Please try again.")
            elif user_input == "2":
                self.admin_question_filter_menu()
>>>>>>> Stashed changes
            elif user_input == "0":
                return
            else:
                print("Wrong input")

<<<<<<< Updated upstream
    def admin_questions_filter_menu(self):
        while True:
            self.header = "Filter questions by..."
=======
    def admin_question_filter_menu(self):
        while True:
            self.header = "Filter questions by"
>>>>>>> Stashed changes
            self.options = ["Status", "Applicants", "School", "Mentor", "Date"]
            self.exit_message = "Back"
            self.print_menu()

<<<<<<< Updated upstream
            user_input = input("Please choose an option: ")
=======
            user_input = input("Please choose an option:")
>>>>>>> Stashed changes

            if user_input == "1":
                print("something")
            elif user_input == "2":
                print("something")
            elif user_input == "3":
                print("something")
            elif user_input == "4":
                print("something")
            elif user_input == "5":
                print("something")
            elif user_input == "0":
                return
            else:
                print("Wrong input")

    def interface_flow(self):
        self.main_menu()
<<<<<<< Updated upstream


ui = Menu()
ui.interface_flow()
=======
>>>>>>> Stashed changes
