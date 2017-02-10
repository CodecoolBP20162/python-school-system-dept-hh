from ui import Menu

class Main:

    def __init__(self):
        self.ui = Menu()



    def run(self):
        self.ui.interface_flow()


Main().run()