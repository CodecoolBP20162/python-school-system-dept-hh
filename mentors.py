from models import *


class Mentors:


    @staticmethod
    def check_mentors_interviews(id_input):

        interview_list = []

        mentors_interview = Interview.select()

        for interview in mentors_interview:
            if interview.interviewslot.mentor.id == int(id_input):
                interview_list.append(interview)

        print("**************YOUR INTERVIEWS**************\n")

        for interviews in interview_list:
            print("Your interview starts at {start}\n".format(start=interviews.interviewslot.start))
            print("Your interview ends at {end}\n".format(end=interviews.interviewslot.end))
            print("Applicant's name: {applicant}\n".format(applicant=interviews.applicant.name))
            print("Applicant's code: {code}\n".format(code=interviews.applicant.code))



        print("*******************************************\n")

        if len(interview_list) == 0:
            print("YOU DON'T HAVE ANY INTERVIEWS.")
