
from models.user import User
from models.tutor import Tutor
from models.student import Student
from models.lessons import Lesson
from models.funcs import query_lessons, tutor_lesson_delete, \
    get_tutor, get_student, get_persons

persons_dict = {
    'tutor': {
        'obj': Tutor,
        'getter': get_tutor,
        'name': 'tutor_name'
    },
    'student': {
        'obj': Student,
        'getter': get_student,
        'name': 'student_name'
    }
}