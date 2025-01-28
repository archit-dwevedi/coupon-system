from user import Customer

class UserGroup:

    def __init__(self, name):
        self.name = name
        self.users = []

    def add_user(self, user: Customer):
        self.users.append(user)

    



    