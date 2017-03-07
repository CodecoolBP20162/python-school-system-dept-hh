from models import *


class MentorsIterable:
    def __init__(self, mentors=Mentor.select().join(School)):
        self.mentors = mentors

    def __iter__(self):
        return MentorsIterator(self.mentors)


class MentorsIterator:
    def __init__(self, mentors):
        self.results = [[mentor.name, mentor.email, mentor.password,
                         mentor.related_school.name] for mentor in mentors]
        self.index = 0

    def __next__(self):
        if self.index == len(self.results):
            raise StopIteration()
        element = self.results[self.index]
        self.index += 1
        return element

    def __iter__(self):
        return self
