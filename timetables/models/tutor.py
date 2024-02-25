
import sqlalchemy as db
from sqlalchemy.orm import relationship
from data_base import Base

class Tutor(Base):

    __tablename__ = 'tutors'

    tutor_id = db.Column(db.String(36), db.ForeignKey('lessons.tutor_id'), primary_key=True)
    tutor_name = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Integer, default=1)
    user_id = db.Column(db.String(36), nullable=False)

    def __repr__(self):
        return f'TUTOR {self.tutor_name}'