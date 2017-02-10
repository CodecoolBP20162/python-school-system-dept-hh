class PrettyTable:
    def __init__(self, table, title_list):
        self.table = table
        self.title_list = title_list
        self.length = []
        self.full_length = 0

    def draw_table(self):

        if len(self.table) != 0:
            for i in range(len(self.title_list)):
                self.length.append(0)
            for i in range(len(self.title_list)):
                self.length[i] = len(self.title_list[i])
                for k in self.table:
                    if len(str(k[i])) > self.length[i]:
                        self.length[i] = len(str(k[i]))

            for i in self.length:
                self.full_length += (i + 1)
            self.full_length -= 1

            startend_line = "-" * self.full_length

            print("/", startend_line, "\\", sep='')

            for i in range(len(self.title_list)):
                print("|", "{text:^{width}}".format(
                    text=self.title_list[i], width=self.length[i]), sep='', end='')
            print("|")

            for i in range(len(self.table)):
                for x in range(len(self.title_list)):
                    mini_line = "-" * self.length[x]
                    print("|", "{text:^{width}}".format(
                        text=mini_line, width=self.length[x]), sep='', end='')
                print("|")
                for y in range(len(self.title_list)):
                    print("|", "{text:^{width}}".format(
                        text=self.table[i][y], width=self.length[y]), sep='', end='')
                print("|")

            print("\\", startend_line, "/", sep='')

        else:
            print("No information to show.")
