
from data_base import sessionmaker

class UserLogin:

    def fromDB(self, user_id):
        self.id = user_id
        return self

    def create(self, user_id):
        self.id = user_id
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)