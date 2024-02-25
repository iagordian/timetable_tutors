
from models.lessons import Lesson
from models.student import Student
from models.tutor import Tutor
from sqlalchemy.orm import Query, Session
from typing import List, NoReturn, Tuple

def query_lessons(tutors: Query, weekday_num: int, db: Session) -> List[dict]:

    '''
    Принимает итерируемый объект тьюторов
    Возвращает список словарей с объектом тьютора
    и всеми его уроками, в которых студенты активные
    '''

    lessons = []

    for tutor in tutors:
        if tutor.active:
            lessons.append({
                'tutor': tutor,
                'lessons': db.query(Lesson).filter(Lesson.student.has(Student.active),
                                                   Lesson.weekday_num==weekday_num,
                                                   Lesson.tutor_id==tutor.tutor_id)
            })

    return lessons

def tutor_lesson_delete(db: Session, just_active=True, **lesson_data) -> NoReturn:

    '''
    Удаление уроков
    По умолчанию удаляет только уроков
    активных тьюторов и учеников
    '''

    lesson_data = {k: v for k, v in lesson_data.items() if k != 'student_id'}
    lessons = db.query(Lesson).filter_by(**lesson_data)

    if just_active:
        lessons = lessons.filter(Lesson.student.has(Student.active),
                                 Lesson.tutor.has(Tutor.active))

    lessons.delete()

def get_persons(user_uid: str, db: Session) -> Tuple[Query]:

    '''
    Возвращает тьюторов и учеников, закрепленных за определенным пользователем
    '''

    tutors = db.query(Tutor).filter(Tutor.user_id == user_uid).order_by(Tutor.tutor_name)
    students = db.query(Student).filter(Student.user_id == user_uid).order_by(Student.student_name)

    return tutors, students

def get_tutor(tutor_id: str, db: Session) -> Tutor:
    return db.query(Tutor).filter_by(tutor_id=tutor_id).first()

def get_student(student_id: str, db: Session) -> Student:
    return db.query(Student).filter_by(student_id=student_id).first()




