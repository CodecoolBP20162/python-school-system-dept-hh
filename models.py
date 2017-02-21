from peewee import *

identify = open("parameter.txt", "r")
login = identify.readlines()
identify.close()

db = PostgresqlDatabase('dry', user='dry')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class School(BaseModel):
    name = CharField()


class City(BaseModel):
    name = CharField()
    related_school = ForeignKeyField(School, related_name="cities")


class Mentor(BaseModel):
    name = CharField()
    email = CharField()
    related_school = ForeignKeyField(School, related_name="workplaces")


class Applicant(BaseModel):
    name = CharField()
    city = ForeignKeyField(City, related_name="homes")
    status = CharField()
    code = CharField()
    email = CharField()
    school = ForeignKeyField(School, related_name="registered_schools")


class InterviewSlot(BaseModel):
    start = DateTimeField()
    end = DateTimeField()
    reserved = BooleanField()
    mentor = ForeignKeyField(Mentor, related_name="mentors")
    mentor2 = ForeignKeyField(Mentor)


class Interview(BaseModel):
    applicant = ForeignKeyField(Applicant, related_name="interviews")
    interviewslot = ForeignKeyField(InterviewSlot, related_name="interviews")


class Question(BaseModel):
    question = TextField()
    applicant = ForeignKeyField(Applicant, related_name="questions")
    status = CharField()
    chosenmentor = ForeignKeyField(Mentor, related_name="questions", null=True)
    submissiondate = DateTimeField()


class Answer(BaseModel):
    answer = TextField()
    question = ForeignKeyField(Question, related_name="questions")


class Email(BaseModel):
    subject = CharField()
    message = TextField()
    type = CharField()
    submissiondate = DateTimeField()
    recipient_name = CharField(max_length=10000)
    recipient_email = CharField(max_length=10000)
