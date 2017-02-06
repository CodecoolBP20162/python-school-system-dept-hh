# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!
import random
from models import *
import datetime


class Newapplicants:
    @staticmethod
    def check_applicant(code_input):

        app_datas = Applicant.select().where(Applicant.code == code_input).get()

        return app_datas

    @staticmethod
    def check_applicant_interview(code_input):

        app_interview_datas = (InterviewSlot
                               .select()
                               .join(Interview)
                               .join(Applicant)
                               .where(Applicant.code == code_input)).get()

        return app_interview_datas

    @staticmethod
    def data_for_new_applicant():

        app_inputs_list = []

        app_inputs_list.append(input("Please enter your name:"))
        app_inputs_list.append(input("Please enter your city:"))

        available_cities = []
        for city in City.select():
            available_cities.append(city.name)

        if app_inputs_list[1] not in available_cities:
            print("\nSorry, your city is not in our database, but we're working on it!")
            return None

        else:
            app_inputs_list.append(input("Please enter your e-mail:"))
            return app_inputs_list

    @staticmethod
    def new_applicant(app_data_list):
        if len(app_data_list) == 3:
            new_applicant_city = City.select().where(City.name == app_data_list[1]).get()
            applicant_school = new_applicant_city.related_school

            new_applicant = Applicant.create(name=app_data_list[0], city=new_applicant_city, school=applicant_school,
                                             status="new", code=Newapplicants.random_app_code(), email=app_data_list[2])

            interview_slot = InterviewSlot.select().join(Mentor).where(InterviewSlot.reserved == False,
                                                                       Mentor.related_school == applicant_school).get()

            new_interview = Interview.create(applicant=new_applicant, interviewslot=interview_slot)
            interview_slot.reserved = True

            interview_slot.save()

            return [new_applicant, new_interview]

        else:
            pass

    @staticmethod
    def random_app_code():
        digits = "0123456789"
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        charlist = []
        charlist.append((random.sample(lowercase, 2)) +
                        (random.sample(uppercase, 2)) +
                        (random.sample(digits, 2)))

        random.shuffle(charlist[0])
        rand_code = "".join(charlist[0])

        code_table = Applicant.select().where(Applicant.code == rand_code)  # CHECK FOR EQUALITY

        if len(code_table) > 0:
            Newapplicants.random_app_code()

        return rand_code

    @staticmethod
    def add_question_to_database():
        question_list = []
        question_list.append(input("Add your code:"))
        question_list.append(input("Your question:"))

        applicant = Applicant.get(Applicant.code == question_list[0])

        Question.create(question=question_list[1], applicant_id=applicant, status="new",
                        chosenmentor_id=None, submissiondate=datetime.datetime.now())

    @staticmethod
    def get_question_info():

        identify_applicant = input("Add your code:")
        applicant = Applicant.get(Applicant.code == identify_applicant)


        questiondata = []

        for question in applicant.questions:

            try:
                answer = Answer.get(Answer.question_id == question)
                questiondata.append([question.question, question.status, answer.answer])
            except:
                questiondata.append([question.question, question.status, "no answer yet"])

        return questiondata



