from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id=0):
        super().__init__()
        self.id = id

    def get_id(self):
        return super().get_id()
