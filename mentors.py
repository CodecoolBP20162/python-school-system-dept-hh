from models import *

class Mentors:

    @staticmethod
    def check_mentors_interviews(name_input):

        interview_list = []

        mentors_interview = (Interview
                   .select()
                    .join(InterviewSlot, JOIN.LEFT_OUTER)
                   .where(InterviewSlot.mentor_id == name_input))
        print(mentors_interview)
        for n in mentors_interview:
            print(interview_list.append([n.start,n.end,n.reserver]))


        print("**************YOUR INTERVIEWS**************\n")

        for interviews in interview_list:

            print("Your interview starts: {start}\n".format(start = interviews[0]))
            print("Your interview ends: {end}\n".format(end=interviews[1]))
            print("Reserved: {is_reserved}\n".format(is_reserved=interviews[2]))


            print("_______________________" + "_" * len(str(interviews[0])))

        print("*******************************************\n")

        if len(interview_list) == 0:
            print("YOU DON'T HAVE ANY INTERVIEWS.")

