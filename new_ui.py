# from administrator import AdministratorData
# from mentor import MentorData
# from applicants import ApplicantData


class Menu:

    def __init__(self):
        self.header = None
        self.options = None
        self.exit_message = None

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

            user_input = input("Please choose a role:")

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

            user_input = input("Please choose an option:")

            if user_input = "1":
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

            user_input = input("Please choose an option:")

            if user_input == "0":
                return
            else:
                print("Wrong input")

    def admin_menu(self):
        while True:
            self.header = "Applciant menu"
            self.options = ["Applicants", "Interviews",
                            "Questions"]
            self.exit_message = "Back"
            self.print_menu()

            user_input = input("Please choose an option:")

            if user_input == "0":
                return
            else:
                print("Wrong input")

    def interface_flow(self):
        self.main_menu()


ui = Menu()
ui.interface_flow()
