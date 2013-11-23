"""
daeta module. more to come
"""


class Stash(object):

    def __init__(self, name):
        self.name = name
        self._items = []

    def add(self, item):
        self._items.append(item)

    def all(self):
        return self._items