from models import *

class Administrator:

    @staticmethod
    def applicants_personal_data():

        tags = ["ID","Name","CityID","Status","Code","SchoolID"]
        apps_personal_data = []

        applicants = Applicant.select()

        for apps in applicants:
                apps_personal_data.append([apps.id,apps.name,apps.city.name,apps.status,apps.code,apps.school.name])

        Administrator.prettytable(apps_personal_data,tags)
        """        print("**************APPLICANTS TABLE**************\n")

                for app_data in apps_personal_data:
                    print("ID {id}\n".format(id=app.interviewslot.start))
                    print("Your interview ends at {end}\n".format(end=interviews.interviewslot.end))
                    print("Applicant's name: {applicant}\n".format(applicant=interviews.applicant.name))
                    print("Applicant's code: {code}\n".format(code=interviews.applicant.code))

                print("*******************************************\n")
        """

    @staticmethod
    def prettytable(table, title_list):

        length = []
        for i in range(len(title_list)):
            length.append(0)
        for i in range(len(title_list)):
            length[i] = len(title_list[i])
            for k in table:
                if len(str(k[i])) > length[i]:
                    length[i] = len(str(k[i]))

        # width of the full table
        full_length = 0
        for i in length:
            full_length += (i + 1)
        full_length -= 1

        startend_line = "-" * full_length

        # upper grid
        print("/", startend_line, "\\", sep='')

        # title list
        for i in range(len(title_list)):
            print("|", "{text:^{width}}".format(
                text=title_list[i], width=length[i]), sep='', end='')
        print("|")

        # table
        for i in range(len(table)):
            for x in range(len(title_list)):
                mini_line = "-" * length[x]
                print("|", "{text:^{width}}".format(
                    text=mini_line, width=length[x]), sep='', end='')
            print("|")
            for y in range(len(title_list)):
                print("|", "{text:^{width}}".format(
                    text=table[i][y], width=length[y]), sep='', end='')
            print("|")

        # lower grid
        print("\\", startend_line, "/", sep='')