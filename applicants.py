import random
from models import *
import datetime
from mail import Mail


class ApplicantsData:
    def __init__(self):
        self.query = None
        self.results = []
        self.tags = []

    def check_applicant(self, code_input):

        self.results = []
        self.tags = ['Name', 'City', 'Status', 'School', 'email']
        self.query = Applicant.select().where(Applicant.code == code_input)

        for query_object in self.query:
            self.results.append(
                [query_object.name, query_object.city.name, query_object.status, query_object.school.name,
                 query_object.email])

    def check_applicant_interview(self, code_input):

        self.results = []
        Mentor1 = Mentor.alias()
        Mentor2 = Mentor.alias()
        self.tags = ["Interview date", "Mentor", "Mentor_2", "School"]
        self.query = InterviewSlot.select(InterviewSlot, Mentor1, Mentor2, School).join(Interview).join(
            Applicant).switch(InterviewSlot).join(Mentor1, on=(InterviewSlot.mentor == Mentor1.id)).join(Mentor2, on=(
            InterviewSlot.mentor2 == Mentor2.id)).join(School).where(Applicant.code == code_input)

        for query_object in self.query:
            self.results.append([str(query_object.start), query_object.mentor.name, query_object.mentor2.name,
                                 query_object.mentor.related_school.name])

    def check_city(self, city_input):

        self.results = []
        self.query = City.select(City.name).where(City.name == city_input)

        for query_object in self.query:
            self.results.append([query_object.name])

    @staticmethod
    def email_about_code_and_city_to_applicant(name_input, email_input, application_code, applicant_school):

        recipient_list = [email_input]
        subject = "New Application"
        message = """
        Hi {name_input},
        Your application process to Codecool has been started!
        Your code is {code}, and the city you have been assigned to is {city}.

        Good luck!""".format(name_input=name_input, code=application_code, city=applicant_school.name)

        application_email = Mail(recipient_list, message, subject)
        application_email.send()

    @staticmethod
    def email_about_interview_to_applicant(name_input, email_input, new_interview):

        recipient_list = [email_input]
        subject = "New Interview"
        try:
            message = """
            Hi {name_input},
            Your interview is at {time}, with {mentor} and {mentor2}.
            Please arrive 15 minutes early.

            Good luck!
            """.format(name_input=name_input, time=new_interview.interviewslot.start,
                       mentor=new_interview.interviewslot.mentor.name, mentor2=new_interview.interviewslot.mentor2.name)

        except:
            message = """
            Hi {name_input},
            Our schedule is full, we could not give you an interview date yet.
            If you do not get one within a week, please contact 06-1-1234567.
            Thank you.
            """.format(name_input=name_input)

        interview_email = Mail(recipient_list, message, subject)
        interview_email.send()

    @staticmethod
    def email_about_interview_to_mentor(new_interview):

        recipient_list = [new_interview.interviewslot.mentor.email, new_interview.interviewslot.mentor2.email]
        subject = "You've been assigned to a new interview"
        message = """
        Hi {mentor_name} and {mentor2_name},
        You have been assigned to a new interview from {start} to {end}.
        The applicant's name is {applicant_name}.

        Best regards,
        The Codecool Team
        """.format(mentor_name=new_interview.interviewslot.mentor.name,
                   mentor2_name=new_interview.interviewslot.mentor2.name, start=new_interview.interviewslot.start,
                   end=new_interview.interviewslot.end, applicant_name=new_interview.applicant.name)

        interview_email = Mail(recipient_list, message, subject)
        interview_email.send()

    @staticmethod
    def new_applicant(city_input, name_input, email_input):

        new_applicant_city = City.select().where(City.name == city_input).get()
        applicant_school = new_applicant_city.related_school
        application_code = ApplicantsData.random_app_code()

        new_applicant = Applicant.create(name=name_input, city=new_applicant_city, school=applicant_school,
                                         status="new", code=application_code, email=email_input)

        try:
            interview_slot = InterviewSlot.select().join(Mentor).where(InterviewSlot.reserved == False,
                                                                       Mentor.related_school == applicant_school).get()

            new_interview = Interview.create(applicant=new_applicant, interviewslot=interview_slot)
            interview_slot.reserved = True
            interview_slot.save()

            ApplicantsData.email_about_interview_to_mentor(new_interview)

        except:
            new_interview = None

        ApplicantsData.email_about_code_and_city_to_applicant(name_input, email_input, application_code,
                                                              applicant_school)
        ApplicantsData.email_about_interview_to_applicant(name_input, email_input, new_interview)

        return [new_applicant, new_interview]

    @staticmethod
    def random_app_code():
        digits = "0123456789"
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        charlist = []
        charlist.append((random.sample(lowercase, 1)) +
                        (random.sample(uppercase, 1)) +
                        (random.sample(digits, 2)))

        random.shuffle(charlist[0])
        rand_chars = "".join(charlist[0])

        code_table = Applicant.select(Applicant.id)
        code_list = []
        for ids in code_table:
            code_list.append(ids.id)

        rand_code = str(len(code_list) + 1) + rand_chars

        return rand_code

    def add_question_to_database(self, code_input, question_input):
        self.results = []
        self.query = Applicant.get(Applicant.code == code_input)

        Question.create(question=question_input, applicant_id=self.query.id, status="new",
                        chosenmentor_id=None, submissiondate=datetime.datetime.now())

    def get_question_info(self, code_input):

        self.results = []
        self.tags = ['Question', 'Status', 'Answer']
        self.query = Question.select(Question, Applicant).join(Applicant).where(Applicant.code == code_input)

        for question in self.query:
            answers = Answer.select().where(Answer.question_id == question)
            if len(answers) == 0:
                self.results.append([question.question, question.status, "no answer yet"])
            else:
                for answer in answers:
                    self.results.append([question.question, question.status, answer.answer])
