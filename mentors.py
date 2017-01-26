from models import *


class Mentors:
    @staticmethod
    def check_mentors_interviews(name_input):

        interview_list = []

        mentors_interview = Interview.select()

        for interview in mentors_interview:
            if interview.interviewslot.mentor.name==name_input:
                interview_list.append(interview)

        print("**************YOUR INTERVIEWS**************\n")

        for interviews in interview_list:
            print("Your interview starts: {start}\n".format(start=interviews.interviewslot.start))
            print("Your interview ends: {end}\n".format(end=interviews.interviewslot.end))
            print("Reserved: {is_reserved}\n".format(is_reserved=interviews.interviewslot.reserved))
            print("Reserved: {applicant}\n".format(applicant=interviews.applicant.name))
            print("Applicant's code: {code}\n".format(code=interviews.applicant.code))



        print("*******************************************\n")

        if len(interview_list) == 0:
            print("YOU DON'T HAVE ANY INTERVIEWS.")
