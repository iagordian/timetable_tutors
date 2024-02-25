#from app import db

from werkzeug.security import generate_password_hash

import sqlalchemy as db
from data_base import Base

class User(Base):

    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True)
    login = db.Column(db.String(128), nullable=False)
    _password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, id, login, password):
        self.id = id
        self.login = login
        self.password_hash = password

    def __repr__(self):
        return f'USER {self.login}'

    @property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = generate_password_hash(password)

    @password_hash.deleter
    def password_hash(self):
        del self._password_hash

    @classmethod
    def get_by_login(cls, uid):
        return cls.query.filter_by(id=uid).first()


