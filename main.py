from ui import Menu
from administrator import AdministratorData


# Write here your console application
class Main:
    def __init__(self):
        self.ui = Menu()

    def run(self):
        self.ui.interface_flow()


Main().run()
