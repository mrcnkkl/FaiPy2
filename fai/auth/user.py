from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id=0):
        self.id = str(id)

