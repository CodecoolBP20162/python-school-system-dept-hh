# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!
import random
from models import *


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
    def data_collection():
        app_inputs_list = []
        app_inputs_list.append(str(input("Please enter your name:")))
        app_inputs_list.append(str(input("Please enter your city:")))
        return app_inputs_list

    @staticmethod
    def new_applicant(app_data_list):
        new_applicant_city = City.select().where(City.name == app_data_list[1]).get()
        applicant_school = new_applicant_city.related_school

        new_applicant = Applicant.create(name=app_data_list[0], city=new_applicant_city, school=applicant_school,
                                         status="new", code=Newapplicants.random_app_code())

        interview_slot = InterviewSlot.select().join(Mentor).where(InterviewSlot.reserved == False,Mentor.related_school==applicant_school).get()



        new_interview = Interview.create(applicant=new_applicant, interviewslot=interview_slot)
        interview_slot.reserved = True

        interview_slot.save()

        return [new_applicant, new_interview]

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

        code_table = Applicant.select(Applicant.code)

        # ANOTHER THECNIC
        # code_table = Applicant.select(Applicant.code).where(Applicant.code = rand_code)
        #   if code_table = None:
        #       generate_random()

        for code in code_table:
            if rand_code == code:
                generate_random()

        return rand_code


    @staticmethod
    def add_question_to_database():
        question_list = []
        question_list.append(str(input("Add your code:")))
        question_list.append(str(input("Your question:")))
        print(question_list)
        """
        applicantx = Applicant.select().where(Applicant.code == question_list[
            0])
        print(applicant)
        new_question = Question.create(question=question_list[1], applicant=applicantx.id, status="pending", chosenmentor="no mentor yet")

        questionx = Question.select().where(Question.question == question_list[1])
        new_answer = Answer.create(answer="no answer yet", question_id=questionx.id)
        """

        getapplicant = (Applicant
                               .select()
                               .where(question_list[0] == Applicant.code))
        print(getapplicant.get())

        new_question = Question.create(question=question_list[1], applicant_id=getapplicant, status="pending", chosenmentor_id = None)


    @staticmethod
    def get_question_info():

        identify = input(str("Add your code:"))
        applicant = Applicant.get(Applicant.code == identify)

#        questions = Question.select().where(Question.applicant == applicant)

        for question in applicant.questions:
            print(question.question)
            print(question.status)





