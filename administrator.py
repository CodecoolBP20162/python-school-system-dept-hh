from models import *
import datetime


class Administrator:
    @staticmethod
    def applicants_personal_data():

        tags = ["ID", "Name", "City", "Status", "Code", "School"]
        apps_personal_data = []

        applicants = Applicant.select()

        for apps in applicants:
            apps_personal_data.append([apps.id, apps.name, apps.city.name, apps.status, apps.code, apps.school.name])

        Administrator.prettytable(apps_personal_data, tags)

    @staticmethod
    def apps_by_status(status_filter):

        tags = ["Status", "Name", "Code", "School"]
        apps_personal_data = []

        applicants = Applicant.select().where(Applicant.status == status_filter)

        for apps in applicants:
            apps_personal_data.append([apps.status, apps.name, apps.code, apps.school.name])

        Administrator.prettytable(apps_personal_data, tags)

    @staticmethod
    def apps_by_interview(date_filter):

        tags = ["Name", "Code", "School"]
        filter_transfer = datetime.strptime(date_filter, '%Y-%m-%d %H:%M')
        apps_personal_data = []

        interviews = Interview.select(Interview, InterviewSlot, Applicant, School).join(InterviewSlot).switch(
            Interview).join(Applicant).switch(Applicant).join(School).where(InterviewSlot.start == filter_transfer)

        for interview in interviews:
            apps_personal_data.append(
                [interview.applicant.name, interview.applicant.code,
                 interview.applicant.school.name])

        Administrator.prettytable(apps_personal_data, tags)

    @staticmethod
    def apps_by_location(location_filter):

        tags = ["School", "Name", "Code"]
        apps_personal_data = []

        applicants = Applicant.select().join(School).where(School.name == location_filter)

        for apps in applicants:
            apps_personal_data.append([apps.school.name, apps.name, apps.code])

        Administrator.prettytable(apps_personal_data, tags)

    @staticmethod
    def apps_by_city(city_filter):

        tags = ["City", "Name", "Code"]
        apps_personal_data = []

        applicants = Applicant.select().join(City).where(City.name == city_filter)

        for apps in applicants:
            apps_personal_data.append([apps.city.name, apps.name, apps.code])

        Administrator.prettytable(apps_personal_data, tags)

    @staticmethod
    def apps_by_mentor(mentor_filter):

        tags = ["Mentor", "Applicant name", "Code"]
        apps_personal_data = []

        interviews = Interview.select(Applicant, Interview, InterviewSlot, Mentor).join(Applicant).switch(
            Interview).join(InterviewSlot).join(Mentor).where(Mentor.name == mentor_filter)

        for interview in interviews:
            apps_personal_data.append(
                [interview.interviewslot.mentor.name, interview.applicant.name, interview.applicant.code])

        Administrator.prettytable(apps_personal_data, tags)

    @staticmethod
    def emails_by_names(app_id):

        tags = ["Name", "Email"]
        apps_personal_data = []

        applicants = Applicant.select().where(Applicant.id == app_id)

        for apps in applicants:
            apps_personal_data.append([apps.name, apps.email])

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
    def listing_interviews_by_mentor(mentor_filter):
        interview_list = []
        tags = ["School", "Applicant code", "Date"]

        interview_query = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(Mentor.name == mentor_filter)
        for interview in interview_query:
            interview_list.append([interview.interviewslot.mentor.related_school.name, interview.applicant.code,
                                   str(interview.interviewslot.start)])

        Administrator.prettytable(interview_list, tags)

    @staticmethod
    def listing_interviews_by_applicant_code(code_filter):
        interview_list = []
        tags = ["School", "Mentor", "Date"]

        interview_query_list = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(Applicant.code == code_filter)
        for interview in interview_query_list:
            interview_list.append(
                [interview.interviewslot.mentor.related_school.name, interview.interviewslot.mentor.name,
                 str(interview.interviewslot.start)])

        Administrator.prettytable(interview_list, tags)

    @staticmethod
    def listing_interviews_by_school(school_filter):
        interview_list = []
        tags = ["Applicant code", "Mentor", "Date"]

        interview_query_list = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(School.name == school_filter)
        for interview in interview_query_list:
            interview_list.append([interview.applicant.code,
                                   interview.interviewslot.mentor.name, str(interview.interviewslot.start)])

        Administrator.prettytable(interview_list, tags)

    @staticmethod
    def listing_interviews_by_date(date_filter):
        interview_list = []
        filter_transfer = datetime.datetime.strptime(date_filter, '%Y-%m-%d')
        tags = ["School", "Applicant code", "Mentor"]

        interview_query_list = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(

            School).switch(Interview).join(InterviewSlot).join(Mentor).where(InterviewSlot.start.between(datetime.datetime.combine(filter_transfer, datetime.time.min),datetime.datetime.combine(filter_transfer, datetime.time.max)))

        for interview in interview_query_list:
            interview_list.append([interview.interviewslot.mentor.related_school.name, interview.applicant.code,
                                   interview.interviewslot.mentor.name])

        Administrator.prettytable(interview_list, tags)

    @staticmethod
    def mentor_assigning():

        identify_mentor = input("Choose mentor ID:")
        identify_question = input("Choose question ID:")

        mentor = Mentor.select().where(Mentor.id == int(identify_mentor))
        question = Question.get(Question.id == int(identify_question))

        question.chosenmentor = mentor
        question.status = "waiting for answer"
        question.save()

    @staticmethod
    def question_by_status(status_filter):

        tags = ["Status", "Question"]

        questions_data = []

        questions = Question.select().where(Question.status == status_filter)

        for question in questions:
            questions_data.append([question.status, question.question])

        Administrator.prettytable(questions_data, tags)

    @staticmethod
    def question_by_applicants(app_filter):

        tags = ["QuestionID", "Question", "Application name", "Application code"]

        questions_data = []

        questions = Question.select().join(Applicant).where(Applicant.name == app_filter)

        for question in questions:
            questions_data.append([question.id, question.question, question.applicant.name, question.applicant.code])

        Administrator.prettytable(questions_data, tags)

    @staticmethod
    def question_by_school(school_filter):

        tags = ["QuestionID", "Question", "School"]

        questions_data = []

        questions = Question.select().join(Applicant).join(School).where(School.name == school_filter)

        for question in questions:
            questions_data.append([question.id, question.question, question.applicant.school.name])

        Administrator.prettytable(questions_data, tags)

    @staticmethod
    def question_by_mentor(mentor_filter):

        tags = ["QuestionID", "Question", "Mentor"]

        questions_data = []

        questions = Question.select().join(Mentor).where(Mentor.name == mentor_filter)

        for question in questions:
            questions_data.append([question.id, question.question, question.chosenmentor.name])

        Administrator.prettytable(questions_data, tags)

    @staticmethod
    def question_by_date(date_filter):
        question_list = []
        filter_transfer = datetime.strptime(date_filter, '%Y-%m-%d %H:%M')
        tags = ["QuestionID", "Question"]

        questions = Question.select().where(Question.submissiondate == filter_transfer)

        for question in questions:
            question_list.append([question.id, question.question])

        Administrator.prettytable(question_list, tags)

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
