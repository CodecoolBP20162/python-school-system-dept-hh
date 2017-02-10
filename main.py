from ui import Menu


class Main:
    def __init__(self):
        self.ui = Menu()

    def run(self):
        self.ui.main_menu()


Main().run()
