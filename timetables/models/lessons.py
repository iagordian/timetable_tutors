
import sqlalchemy as db
from data_base import Base
from sqlalchemy.orm import relationship, backref

class Lesson(Base):

    __tablename__ = 'lessons'

    tutor_id = db.Column(db.String(36), primary_key=True)
    student_id = db.Column(db.String(36), primary_key=True)
    weekday_num = db.Column(db.Integer, primary_key=True)
    lesson_num = db.Column(db.Integer, primary_key=True)

    student = relationship('Student', backref="lessons", uselist=False)
    tutor = relationship('Tutor', backref="lessons", uselist=False)

    def __repr__(self):
        return f'LESSON {self.weekday_num} {self.lesson_num}'