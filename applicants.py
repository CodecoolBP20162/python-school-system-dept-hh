# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!
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
        self.tags = ['Name','City','Status','School','email']
        self.query = Applicant.select().where(Applicant.code == code_input)

        for query_object in self.query:

            self.results.append([query_object.name,query_object.city.name,query_object.status,query_object.school.name,query_object.email])

    def check_applicant_interview(self, code_input):

        self.results = []
        self.tags = ["Interview date", "Mentor", "School"]

        self.query = InterviewSlot.select(InterviewSlot.start,Mentor.name,School.name).join(Interview).join(Applicant).switch(InterviewSlot).join(Mentor).join(School).where(Applicant.code == code_input)

        for query_object in self.query:
            self.results.append([query_object.start, query_object.mentor.name, query_object.mentor.related_school.name])


    def check_city(self, city_input):

        self.results = []

        self.query = City.select(City.name).where(City.name == city_input)

        for query_object in self.query:
            self.results.append([query_object.name])


    @staticmethod
    def email_about_code_and_city(name_input, email_input, application_code, applicant_school):

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
    def new_applicant(city_input, name_input, email_input):

        new_applicant_city = City.select().where(City.name == city_input).get()
        applicant_school = new_applicant_city.related_school
        application_code = ApplicantsData.random_app_code()

        new_applicant = Applicant.create(name=name_input, city=new_applicant_city, school=applicant_school,
                                         status="new", code=application_code, email=email_input)

        interview_slot = InterviewSlot.select().join(Mentor).where(InterviewSlot.reserved == False,
                                                                   Mentor.related_school == applicant_school).get()

        new_interview = Interview.create(applicant=new_applicant, interviewslot=interview_slot)
        interview_slot.reserved = True

        interview_slot.save()

        ApplicantsData.email_about_code_and_city(name_input, email_input, application_code, applicant_school)

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

        rand_code = str(len(code_list)+1) + rand_chars


        return rand_code

    def add_question_to_database(self, code_input, question_input):

        self.results = []

        self.query = Applicant.select(Applicant.code == code_input).get()

        Question.create(question=question_input, applicant_id=self.query.id, status="new",
                        chosenmentor_id=None, submissiondate=datetime.datetime.now())

    def get_question_info(self, code_input):

        self.results = []

        self.tags = ['Question','Status', 'Answer']

        self.query = Applicant.get(Applicant.code == code_input)

        for question in self.query.questions:

            try:
                answer = Answer.get(Answer.question_id == question)
                self.results.append([question.question, question.status, answer.answer])
            except:
                self.results.append([question.question, question.status, "no answer yet"])