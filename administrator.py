from models import *
import datetime


class AdministratorData:

    def __init__(self):
        self.query = None
        self.results = []
        self.tags = []

    def listing_all_applicants(self):
        self.tags = ["ID", "Name", "City", "Status", "Code", "School"]
        self.query = Applicant.select()
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.id, query_object.name, query_object.city.name, query_object.status, query_object.code,
                 query_object.school.name])

    def applicants_by_status(self, status_filter):
        self.tags = ["Status", "Name", "Code", "School"]
        self.query = Applicant.select().where(Applicant.status == status_filter)
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.status, query_object.name, query_object.code, query_object.school.name])

    def applicants_by_interview(self, date_filter):
        print(date_filter)
        self.tags = ["Name", "Code", "School"]
        filter_transfer = datetime.datetime.strptime(date_filter, '%Y-%m-%d')
        self.query = Interview.select(Interview, InterviewSlot, Applicant, School).join(InterviewSlot).switch(
            Interview).join(Applicant).switch(Applicant).join(School).where(
            InterviewSlot.start.between(datetime.datetime.combine(filter_transfer, datetime.time.min),
                                        datetime.datetime.combine(filter_transfer, datetime.time.max)))

        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.applicant.name, query_object.applicant.code,
                 query_object.applicant.school.name, str(query_object.interview.interviewslot.start)])

    def applicants_by_location(self, location_filter):
        self.tags = ["School", "Name", "Code"]
        self.query = Applicant.select().join(School).where(School.name == location_filter)
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.school.name, query_object.name, query_object.code])

    def applicants_by_city(self, city_filter):
        self.tags = ["City", "Name", "Code"]
        self.query = Applicant.select().join(City).where(City.name == city_filter)
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.city.name, query_object.name, query_object.code])

    def applicants_by_mentor(self, mentor_filter):
        self.tags = ["Mentor", "Applicant name", "Code"]
        self.query = Interview.select(Applicant, Interview, InterviewSlot, Mentor).join(Applicant).switch(
            Interview).join(InterviewSlot).join(Mentor).where(Mentor.name == mentor_filter)
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.interviewslot.mentor.name, query_object.applicant.name, query_object.applicant.code])

    def applicant_email_by_applicant_code(self, applicant_code):
        self.tags = ["Name", "Email"]
        self.query = Applicant.select().where(Applicant.code == applicant_code)
        self.results = []

        for query_object in self.query:
            self.results.append([query_object.name, query_object.email])

    def listing_all_interviews(self):
        self.tags = ["School", "Applicant code", "Mentor", "Date"]
        self.query = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor)
        self.results = []

        for query_object in self.query:
            self.results.append([query_object.interviewslot.mentor.related_school.name, query_object.applicant.code,
                                 query_object.interviewslot.mentor.name, str(query_object.interviewslot.start)])

    def listing_interviews_by_mentor(self, mentor_filter):
        self.tags = ["School", "Applicant code", "Date"]
        self.query = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(Mentor.name == mentor_filter)
        self.results = []

        for query_object in self.query:
            self.results.append([query_object.interviewslot.mentor.related_school.name, query_object.applicant.code,
                                 str(query_object.interviewslot.start)])

    def listing_interviews_by_applicant_code(self, code_filter):
        self.tags = ["School", "Mentor", "Date"]
        self.query = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(Applicant.code == code_filter)
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.interviewslot.mentor.related_school.name, query_object.interviewslot.mentor.name,
                 str(query_object.interviewslot.start)])

    def listing_interviews_by_school(self, school_filter):
        self.tags = ["Applicant code", "Mentor", "Date"]
        self.query = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(School.name == school_filter)
        self.results = []

        for query_object in self.query:
            self.results.append([query_object.applicant.code,
                                 query_object.interviewslot.mentor.name, str(query_object.interviewslot.start)])

    def listing_interviews_by_date(self, date_filter):
        filter_transfer = datetime.datetime.strptime(date_filter, '%Y-%m-%d')
        self.tags = ["School", "Applicant code", "Mentor","Date"]
        self.query = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(
            InterviewSlot.start.between(datetime.datetime.combine(filter_transfer, datetime.time.min),
                                        datetime.datetime.combine(filter_transfer, datetime.time.max)))
        self.results = []

        for query_object in self.query:
            self.results.append([query_object.interviewslot.mentor.related_school.name, query_object.applicant.code,
                                 query_object.interviewslot.mentor.name,str(query_object.interviewslot.start)])

    @staticmethod
    def assign_mentor_to_question(choosen_mentor, choosen_question):
        mentor = Mentor.get(Mentor.id == int(choosen_mentor))
        question = Question.get(Question.id == int(choosen_question))
        question.chosenmentor = mentor
        question.status = "waiting for answer"
        question.save()

    def question_by_status(self, status_filter):
        self.tags = ["Status", "Question"]
        self.query = Question.select().where(Question.status == status_filter)
        self.results = []

        for query_object in self.query:
            self.results.append([query_object.status, query_object.question])

    def question_by_applicants(self, applicant_filter):
        self.tags = ["QuestionID", "Question",
                     "Application name", "Application code"]
        self.query = Question.select().join(Applicant).where(
            Applicant.name == applicant_filter)
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.id, query_object.question, query_object.applicant.name, query_object.applicant.code])

    def question_by_school(self, school_filter):
        self.tags = ["QuestionID", "Question", "School"]
        self.query = Question.select().join(Applicant).join(
            School).where(School.name == school_filter)
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.id, query_object.question, query_object.applicant.school.name])

    def question_by_mentor(self, mentor_filter):
        self.tags = ["QuestionID", "Question", "Mentor"]
        self.query = Question.select().join(Mentor).where(Mentor.name == mentor_filter)
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.id, query_object.question, query_object.chosenmentor.name])

    def question_by_date(self, date_filter):
        filter_transfer = datetime.datetime.strptime(date_filter, '%Y-%m-%d')
        self.tags = ["QuestionID", "Question"]
        self.query = Question.select().where(
            Question.submissiondate.beetween(datetime.datetime.combine(filter_transfer, datetime.time.min),
                                             datetime.datetime.combine(filter_transfer, datetime.time.max)))
        self.results = []

        for query_object in self.query:
            self.results.append([query_object.id, query_object.question])
