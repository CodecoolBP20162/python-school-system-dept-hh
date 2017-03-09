from models import *

class MentorsData:


    def __init__(self):
        self.query = None
        self.results = []
        self.tags = []

    def mentors_interviews_data(self, mentor_id):
        self.tags = ["Start", "End", "Applicant", "Code"]
        self.query = Interview.select().join(InterviewSlot).where(
            (InterviewSlot.mentor == mentor_id) | (InterviewSlot.mentor2 == mentor_id))
        self.results = []

        for query_object in self.query:
            self.results.append(
                [str(query_object.interviewslot.start), str(query_object.interviewslot.end),
                 query_object.applicant.name,
                 query_object.applicant.code])

    def question_data(self, mentor_id):
        self.tags = ["ID", "Question", "Application code", "Submission date"]
        self.query = Question.select().join(Mentor).where(
            (Mentor.id == mentor_id) & (Question.status == "waiting for answer"))
        self.results = []

        for question in self.query:
            self.results.append([question.id, question.question, question.applicant.code, str(
                question.submissiondate)])

    @staticmethod
    def question_answering(question_id, answer):

        question = Question.get(Question.id == int(question_id))
        Answer.create(answer=answer, question=question)

        question.status = "answered"
        question.save()
