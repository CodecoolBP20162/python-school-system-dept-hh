from ui import Menu
from administrator import AdministratorData

# Write here your console application
class Main:

    ui = None

    @classmethod
    def initialize_menu(cls):
        cls.ui = Menu()


    @classmethod
    def run(cls):
        if cls.ui is None:
            cls.initialize_menu()
        cls.ui.interface_flow()


Main.run()


