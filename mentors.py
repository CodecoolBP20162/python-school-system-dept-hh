from models import *


class MentorsData:
    def __init__(self):
        self.query = None
        self.results = []
        self.tags = []

    def mentors_interviews_data(self, mentor_id):
        self.tags = ["Start", "End", "Applicant", "Code"]
        self.query = Interview.select()
        self.results = []

        for query_object in self.query:
            if query_object.interviewslot.mentor.id == int(mentor_id):
                self.results.append(
                    [query_object.interviewslot.start, query_object.interviewslot.end, query_object.applicant.name,
                     query_object.applicant.code])

    def question_data(self, mentor_id):
        self.tags = ["Submission date", "Question", "Application code", "ID"]
        self.query = Question.select().join(Mentor).where((Mentor.id == mentor_id) & (Question.status == "waiting for answer"))
        self.results = []

        for question in self.query:
            self.results.append([question.submissiondate, question.question, question.applicant.code, question.id])

    @staticmethod
    def question_answering(question_id, answer):

        question = Question.get(Question.id == int(question_id))
        Answer.create(answer=answer, question=question)

        question.status = "answered"
        question.save()

