class Ui:
    @staticmethod
    def interface():

        while True:

            print("\nWelcome to Codecool School System:\n")
            print('''Chose a role:\n
            1. Applicant
            2. Mentor
            3. Administrator
            4. Quit\n''')

            choose = input("Please choose a role:")

            if choose == "1":
                app_inputs_list = []
                app_inputs_list.append(str(input("Please enter your last name:")))
                app_inputs_list.append(str(input("Please enter your city:")))
                print(app_inputs_list)
                return app_inputs_list


            elif choose == "2":
                pass

            elif choose == "3":
                pass

            elif choose == "0":
                exit()
