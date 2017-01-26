from models import *

class Administrator:

    @staticmethod
    def applicants_personal_data():

        tags = ["ID","Name","City","Status","Code","School"]
        apps_personal_data = []

        applicants = Applicant.select()

        for apps in applicants:
                apps_personal_data.append([apps.id,apps.name,apps.city.name,apps.status,apps.code,apps.school.name])

        Administrator.prettytable(apps_personal_data,tags)

    @staticmethod
    def apps_by_status(filter):

        tags = ["Status", "Name", "Code", "School"]
        apps_personal_data = []

        applicants = Applicant.select().where(Applicant.status == filter)

        for apps in applicants:
            apps_personal_data.append([apps.status, apps.name, apps.code, apps.school.name])

        Administrator.prettytable(apps_personal_data, tags)



    @staticmethod
    def apps_by_interview():

        tags = ["Interview starts", "Name", "Code", "School"]
        apps_personal_data = []

        interviews = Interview.select(Interview,InterviewSlot,Applicant,School).join(InterviewSlot).switch(Interview).join(Applicant).switch(Applicant).join(School).where(InterviewSlot.reserved == True)

        for interview in interviews:
            apps_personal_data.append([str(interview.interviewslot.start), interview.applicant.name, interview.applicant.code, interview.applicant.school.name])

        Administrator.prettytable(apps_personal_data, tags)

    @staticmethod
    def apps_by_location(filter):

        tags = ["School", "Name", "Code"]
        apps_personal_data = []

        applicants = Applicant.select().join(School).where(School.name == filter)

        for apps in applicants:
            apps_personal_data.append([apps.school.name, apps.name, apps.code])

        Administrator.prettytable(apps_personal_data, tags)

    @staticmethod
    def apps_by_city(filter):

        tags = ["City", "Name", "Code"]
        apps_personal_data = []

        applicants = Applicant.select().join(City).where(City.name == filter)

        for apps in applicants:
            apps_personal_data.append([apps.city.name, apps.name, apps.code])

        Administrator.prettytable(apps_personal_data, tags)

    @staticmethod
    def apps_by_mentor(filter):

        tags = ["Mentor", "Applicant name", "Code"]
        apps_personal_data = []

        interviews = Interview.select(Applicant,Interview,InterviewSlot,Mentor).join(Applicant).switch(Interview).join(InterviewSlot).join(Mentor).where(Mentor.name == filter)

        print(apps_personal_data)

        for interview in interviews:
            apps_personal_data.append([interview.InterviewSlot.mentor.name, interview.applicant.name, interview.applicant.code])

        Administrator.prettytable(apps_personal_data, tags)


    @staticmethod
    def listing_all_interviews():
        interview_list = []
        tags = ["School", "Applicant code", "Mentor", "Date"]

        interview_query_list = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor)
        for interview in interview_query_list:
            interview_list.append([interview.interviewslot.mentor.related_school.name, interview.applicant.code,
                                   interview.interviewslot.mentor.name, str(interview.interviewslot.start)])

        Administrator.prettytable(interview_list, tags)

    @staticmethod
    def listing_interviews_by_mentor(filter):
        interview_list = []
        tags = ["School", "Applicant code", "Date"]

        interview_query = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(Mentor.name == filter)
        for interview in interview_query:
            interview_list.append([interview.interviewslot.mentor.related_school.name, interview.applicant.code,
                                   str(interview.interviewslot.start)])

        Administrator.prettytable(interview_list, tags)

    @staticmethod
    def listing_interviews_by_applicant_code(filter):
        interview_list = []
        tags = ["School", "Mentor", "Date"]

        interview_query_list = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(Applicant.code == filter)
        for interview in interview_query_list:
            interview_list.append(
                [interview.interviewslot.mentor.related_school.name, interview.interviewslot.mentor.name,
                 str(interview.interviewslot.start)])

        Administrator.prettytable(interview_list, tags)

    @staticmethod
    def listing_interviews_by_school(filter):
        interview_list = []
        tags = ["Applicant code", "Mentor", "Date"]

        interview_query_list = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(School.name == filter)
        for interview in interview_query_list:
            interview_list.append([interview.applicant.code,
                                   interview.interviewslot.mentor.name, str(interview.interviewslot.start)])

        Administrator.prettytable(interview_list, tags)

    @staticmethod
    def listing_interviews_by_date(filter):
        interview_list = []
        filter_transfer=datetime.strptime(filter, '%Y-%m-%d %H:%M')
        tags = ["School", "Applicant code", "Mentor"]

        interview_query_list = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(filter_transfer==filter)
        for interview in interview_query_list:
            interview_list.append([interview.interviewslot.mentor.related_school.name, interview.applicant.code,
                                       interview.interviewslot.mentor.name])

        Administrator.prettytable(interview_list, tags)



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