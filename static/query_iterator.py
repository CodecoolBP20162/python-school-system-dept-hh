from models import *


class QueryIterable:

    def __init__(self, query):
        self.query = query

    def __iter__(self):
        return QueryIterator(self.string)


class QueryIterator:
    pass
