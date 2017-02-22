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
        self.tags = ["Status", "ID", "Name", "City", "Code", "School"]
        self.query = Applicant.select().where(Applicant.status.contains(status_filter))
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.status, query_object.id, query_object.name, query_object.city.name, query_object.code,
                 query_object.school.name])

    def applicants_by_interview(self, date_filter):
        self.tags = ["Name", "Code", "School", "Time"]
        filter_transfer = datetime.datetime.strptime(date_filter, '%Y-%m-%d')
        self.query = Interview.select(Interview, InterviewSlot, Applicant, School).join(InterviewSlot).switch(
            Interview).join(Applicant).switch(Applicant).join(School).where(
            InterviewSlot.start.between(datetime.datetime.combine(filter_transfer, datetime.time.min),
                                        datetime.datetime.combine(filter_transfer, datetime.time.max)))

        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.applicant.name, query_object.applicant.code,
                 query_object.applicant.school.name, str(query_object.interviewslot.start)])

    def applicants_by_location(self, location_filter):
        self.tags = ["School", "ID", "Name", "City", "Status", "Code"]
        self.query = Applicant.select().join(School).where(
            School.name.contains(location_filter))
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.school.name, query_object.id, query_object.name,
                 query_object.city.name, query_object.status, query_object.code, ])

    def applicants_by_city(self, city_filter):
        self.tags = ["City", "ID", "Name", "Status", "Code", "School"]
        self.query = Applicant.select().join(City).where(City.name.contains(city_filter))
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.city.name, query_object.id, query_object.name, query_object.status, query_object.code,
                 query_object.school.name])

    def applicants_by_mentor(self, mentor_filter):
        self.results = []
        self.tags = ["Mentor", "Mentor2", "ID", "Name", "Status", "Code"]
        Mentor1 = Mentor.alias()
        Mentor2 = Mentor.alias()
        self.query = InterviewSlot.select(InterviewSlot, Interview, Mentor1, Mentor2, School).join(Interview).join(
            Applicant).switch(InterviewSlot).join(Mentor1, on=(InterviewSlot.mentor == Mentor1.id)).join(Mentor2, on=(
            InterviewSlot.mentor2 == Mentor2.id)).join(School).where(
            (Mentor1.name.contains(mentor_filter)) | (Mentor2.name.contains(mentor_filter)))

        for query_object in self.query:
            self.results.append(
                [query_object.mentor.name, query_object.mentor2.name,
                 query_object.interview.applicant.id, query_object.interview.applicant.status,
                 query_object.interview.applicant.name, query_object.interview.applicant.code])

    def applicant_email_by_applicant_code(self, applicant_code):
        self.tags = ["ID", "Name", "Email", "Status", "School", "Code"]
        self.query = Applicant.select().where(Applicant.code.contains(applicant_code))
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.id, query_object.name, query_object.email,
                 query_object.status, query_object.school.name, query_object.code])

    def listing_all_interviews(self):
        self.tags = ["School", "Applicant code", "Mentor", "Mentor2", "Date"]
        Mentor1 = Mentor.alias()
        Mentor2 = Mentor.alias()
        self.query = InterviewSlot.select(InterviewSlot, Interview, Mentor1, Mentor2, School).join(Interview).join(
            Applicant).switch(InterviewSlot).join(Mentor1, on=(InterviewSlot.mentor == Mentor1.id)).join(Mentor2, on=(
            InterviewSlot.mentor2 == Mentor2.id)).join(School)

        self.results = []

        for query_object in self.query:
            self.results.append([query_object.mentor.related_school.name, query_object.interview.applicant.code, query_object.mentor.name, query_object.mentor2.name, str(query_object.start)])

    def listing_interviews_by_mentor(self, mentor_filter):
        self.tags = ["Mentor1", "Mentor2", "School", "Applicant code", "Date"]
        Mentor1 = Mentor.alias()
        Mentor2 = Mentor.alias()
        self.query = InterviewSlot.select(InterviewSlot, Interview, Mentor1, Mentor2, School).join(Interview).join(
            Applicant).switch(InterviewSlot).join(Mentor1, on=(InterviewSlot.mentor == Mentor1.id)).join(Mentor2, on=(
            InterviewSlot.mentor2 == Mentor2.id)).join(School).where(
            (Mentor1.name.contains(mentor_filter)) | (Mentor2.name.contains(mentor_filter)))
        self.results = []

        for query_object in self.query:
            self.results.append([query_object.mentor.name, query_object.mentor2.name, query_object.mentor.related_school.name, query_object.interview.applicant.code, str(query_object.start)])

    def listing_interviews_by_applicant_code(self, code_filter):
        self.tags = ["Applicant code", "School", "Mentor", "Mentor2", "Date"]
        Mentor1 = Mentor.alias()
        Mentor2 = Mentor.alias()
        self.query = InterviewSlot.select(InterviewSlot, Interview, Mentor1, Mentor2, School).join(Interview).join(
            Applicant).switch(InterviewSlot).join(Mentor1, on=(InterviewSlot.mentor == Mentor1.id)).join(Mentor2, on=(
            InterviewSlot.mentor2 == Mentor2.id)).join(School).where(Applicant.code.contains(code_filter))
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.interview.applicant.code, query_object.mentor.related_school.name, query_object.mentor.name, query_object.mentor2.name,
                 str(query_object.start)])

    def listing_interviews_by_school(self, school_filter):

        self.tags = ["School", "Applicant code", "Mentor", "Mentor2", "Date"]

        Mentor1 = Mentor.alias()
        Mentor2 = Mentor.alias()
        self.query = InterviewSlot.select(InterviewSlot, Interview, Mentor1, Mentor2, School).join(Interview).join(
            Applicant).switch(InterviewSlot).join(Mentor1, on=(InterviewSlot.mentor == Mentor1.id)).join(Mentor2, on=(
            InterviewSlot.mentor2 == Mentor2.id)).join(School).where(School.name.contains(school_filter))
        self.results = []

        for query_object in self.query:
            self.results.append([query_object.mentor.related_school.name, query_object.interview.applicant.code, query_object.mentor.name, query_object.mentor2.name, str(query_object.start)])

    def listing_interviews_by_date(self, date_filter):
        self.results = []
        filter_transfer = datetime.datetime.strptime(date_filter, '%Y-%m-%d')
        self.tags = ["Date", "School", "Applicant code", "Mentor", "Mentor2"]
        self.query = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(
            InterviewSlot.start.between(datetime.datetime.combine(filter_transfer, datetime.time.min),
                                        datetime.datetime.combine(filter_transfer, datetime.time.max)))

        for query_object in self.query:
            self.results.append([str(query_object.interviewslot.start), query_object.interviewslot.mentor.related_school.name, query_object.applicant.code,
                                 query_object.interviewslot.mentor.name, query_object.interviewslot.mentor2.name])

    @staticmethod
    def assign_mentor_to_question(choosen_mentor, choosen_question):
        mentor = Mentor.get(Mentor.id == int(choosen_mentor))
        question = Question.get(Question.id == int(choosen_question))
        question.chosenmentor = mentor
        question.status = "waiting for answer"
        question.save()

    def question_by_status(self, status_filter):
        self.tags = ["QuestionID", "Status", "Question",
                     "Applicant code", "Date", "School"]
        self.query = Question.select().where(Question.status == status_filter)
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.id, query_object.status, query_object.question, query_object.applicant.code,
                 str(query_object.submissiondate), query_object.applicant.school.name])

    def question_by_applicants(self, applicant_filter):
        self.tags = ["QuestionID", "Question",
                     "Application name", "Application code"]
        self.query = Question.select().join(Applicant).where(
            Applicant.code == applicant_filter)
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
        self.tags = ["QuestionID", "Applicant code", "Question", "Mentor"]
        self.query = Question.select().join(Mentor).where(Mentor.name == mentor_filter)
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.id, query_object.applicant.code, query_object.question, query_object.chosenmentor.name])

    def question_by_date(self, date_filter):
        filter_transfer = datetime.datetime.strptime(date_filter, '%Y-%m-%d')
        self.tags = ["QuestionID", "Question", "Applicant code"]
        self.query = Question.select().where(
            Question.submissiondate.between(datetime.datetime.combine(filter_transfer, datetime.time.min),
                                            datetime.datetime.combine(filter_transfer, datetime.time.max)))
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.id, query_object.question, query_object.applicant.code])
            self.results.append(
                [query_object.id, query_object.question, query_object.applicant.code])

    def listing_all_emails(self):
        self.tags = ["Subject", "Message", "Type", "Submission Date",
                     "Recipient's name", "Recipient's e-mail"]
        self.query = Email.select()
        self.results = []

        for query_object in self.query:
            self.results.append(
                [query_object.subject, query_object.message, query_object.type, query_object.submissiondate, query_object.recipient_name,
                 query_object.recipient_email])
