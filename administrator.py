from models import *
from datetime import datetime

class Administrator:
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
    def listing_interviews_by_mentor(filter):
        interview_list = []
        tags = ["School", "Applicant code", "Date"]

        interview_query = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(Mentor.name == filter)
        for interview in interview_query:
            interview_list.append([interview.interviewslot.mentor.related_school.name, interview.applicant.code,
                                   str(interview.interviewslot.start)])

        Administrator.prettytable(interview_list, tags)

    @staticmethod
    def listing_interviews_by_applicant_code(filter):
        interview_list = []
        tags = ["School", "Mentor", "Date"]

        interview_query_list = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(Applicant.code == filter)
        for interview in interview_query_list:
            interview_list.append(
                [interview.interviewslot.mentor.related_school.name, interview.interviewslot.mentor.name,
                 str(interview.interviewslot.start)])

        Administrator.prettytable(interview_list, tags)

    @staticmethod
    def listing_interviews_by_school(filter):
        interview_list = []
        tags = ["Applicant code", "Mentor", "Date"]

        interview_query_list = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(School.name == filter)
        for interview in interview_query_list:
            interview_list.append([interview.applicant.code,
                                   interview.interviewslot.mentor.name, str(interview.interviewslot.start)])

        Administrator.prettytable(interview_list, tags)

    @staticmethod
    def listing_interviews_by_date(filter):
        interview_list = []
        filter_transfer=datetime.strptime(filter, '%Y-%m-%d %H:%M')
        tags = ["School", "Applicant code", "Mentor"]

        interview_query_list = Interview.select(Interview, School, Applicant, InterviewSlot).join(Applicant).join(
            School).switch(Interview).join(InterviewSlot).join(Mentor).where(filter_transfer==filter)
        for interview in interview_query_list:
            interview_list.append([interview.interviewslot.mentor.related_school.name, interview.applicant.code,
                                       interview.interviewslot.mentor.name])

        Administrator.prettytable(interview_list, tags)

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
        print("\\", startend_line, "/", sep='')
