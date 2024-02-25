
import sqlalchemy as db
from data_base import Base

class Student(Base):

    __tablename__ = 'students'

    student_id = db.Column(db.String(36), db.ForeignKey('lessons.student_id'), primary_key=True)
    student_name = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Integer, default=1)
    user_id = db.Column(db.String(36), nullable=False)

    def __repr__(self):
        return f'STUDENT {self.student_name}'