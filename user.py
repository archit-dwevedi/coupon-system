from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, name):
        self.name = name


class Customer(User):

    def __init__(self, name):
        super().__init__(name)

class Manager(User):
    pass

