from user import User
from user_group import UserGroup

class UserService:
    _INSTANCE = None

    def __init__(self):
        if UserService._INSTANCE is not None:
            raise Exception("This class is a singleton!")
        
        self.users = {}
        self.user_groups = {}
        
    @staticmethod
    def get_instance(self):
        if UserService._INSTANCE is None:
            UserService._INSTANCE = UserService()
            return UserService._INSTANCE
        return UserService._INSTANCE
    

    def add_user(self, name):
        return User(name=name)

    def add_user_to_group(self, group_id: str, user: User):
        if group_id not in self.user_groups:
            raise Exception("Group not found")

        return self.user_groups[group_id].add_user(user)


    def get_user(self, user_id):
        if user_id not in self.users:
            raise Exception("User not found")
        return self.users[user_id]