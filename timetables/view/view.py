
from view import view_bp
from weekday import Weekday
from timetable import Timetable
from error import error_catch
from models import query_lessons, tutor_lesson_delete, persons_dict, get_persons, Lesson
from request import client_data_catch

from flask import render_template, session, send_file
from flask_login import login_required, current_user

from data_base import sessionmaker

@view_bp.route('/', methods=['GET'])
@login_required
@sessionmaker
def index(db):

    '''
    Рендер главной страницы приложения
    '''

    # Определение дня недели и сохранение в сессию
    weekday = Weekday()
    weekday_num = weekday()
    session['weekday_num'] = weekday_num
    user_uid = current_user.id

    tutors, students = get_persons(user_uid, db)

    lessons = query_lessons(tutors, weekday_num, db)

    timetable = Timetable(lessons, students)
    timetable_html = timetable()

    dataHTML = render_template('/view/main.html', weekday=weekday.label,
                                                  weekdays=weekday.lables,
                                                  weekday_number=weekday_num,
                                                  timetable=timetable_html,
                                                  students=students,
                                                  tutors=tutors)
    return dataHTML

@view_bp.route('/change_weekday/<weekday_num>', methods=['GET'])
@login_required
@error_catch(view_bp)
@sessionmaker
def change_weekday(weekday_num, db):

    '''Принимает новый день недели и сохранение в сессию'''

    weekday = Weekday(weekday_num)
    weekday_num = weekday()
    session['weekday_num'] = weekday_num
    user_uid = current_user.id

    tutors, students = get_persons(user_uid, db)

    lessons = query_lessons(tutors, weekday_num, db)

    timetable = Timetable(lessons, students)
    timetable_html = timetable()

    return {'weekday_title': weekday.label, 'timetable': timetable_html}

@view_bp.route('/save_ceil', methods=['POST'])
@login_required
@error_catch(view_bp)
@client_data_catch
@sessionmaker
def save_lesson(client_data, db):
    '''Сохранение ячейки расписания в БД'''

    client_data['weekday_num'] = session['weekday_num']

    # Удаление другого урока с теми же параметрами
    # Новый урок занимает место старого
    tutor_lesson_delete(db, **client_data, just_active=False)

    if client_data['student_id']:
        lesson = Lesson(**client_data)
        db.add(lesson)

    return {'error': False}

@view_bp.route('/deactivate', methods=['POST'])
@login_required
@error_catch(view_bp)
@client_data_catch
@sessionmaker
def deactivate(client_data, db):

    '''Отключение тьюторов или учащихся или возврат в исходное состояние'''

    person = persons_dict[client_data['person_type']]['getter'](client_data['person_id'], db)
    person.active = client_data['active']
    db.commit()

    user_uid = current_user.id
    tutors, students = get_persons(user_uid, db)

    lessons = query_lessons(tutors, session['weekday_num'], db)

    timetable = Timetable(lessons, students)
    timetable_html = timetable()

    return {'timetable': timetable_html}

@view_bp.route('/clear_timetable', methods=['GET'])
@login_required
@error_catch(view_bp)
@sessionmaker
def clear_timetable(db):
    '''
    Удаление всех уроков определенного дня недели,
    чьи тьюторы и учащиеся активны
    '''
    weekday_num = session['weekday_num']

    tutor_lesson_delete(db, weekday_num=weekday_num)

    user_uid = current_user.id
    tutors, students = get_persons(user_uid, db)

    lessons = query_lessons(tutors, weekday_num, db)

    timetable = Timetable(lessons, students)
    timetable_html = timetable()

    return {'timetable': timetable_html}

@view_bp.route('/clear_column/<lesson_num>', methods=['GET'])
@login_required
@error_catch(view_bp)
@sessionmaker
def clear_column(lesson_num, db):

    '''
    Очиста уроков определенного номера за определенным днем недели
    у активных тьюторов
    '''

    weekday_num = session['weekday_num']

    tutor_lesson_delete(db, weekday_num=weekday_num, lesson_num=lesson_num)

    user_uid = current_user.id
    tutors, students = get_persons(user_uid, db)

    lessons = query_lessons(tutors, weekday_num, db)

    timetable = Timetable(lessons, students)
    timetable_html = timetable()

    return {'timetable': timetable_html}

@view_bp.route('/clear_row/<tutor_id>', methods=['GET'])
@login_required
@error_catch(view_bp)
@sessionmaker
def clear_row(tutor_id, db):
    '''
    Очиста уроков за определенным днем недели
    у конкретного тьюторов
    '''

    weekday_num = session['weekday_num']

    tutor_lesson_delete(db, weekday_num=weekday_num, tutor_id=tutor_id)

    user_uid = current_user.id
    tutors, students = get_persons(user_uid, db)

    lessons = query_lessons(tutors, weekday_num, db)

    timetable = Timetable(lessons, students)
    timetable_html = timetable()

    return {'timetable': timetable_html}

@view_bp.route('/download_timetable', methods=['GET'])
@login_required
@error_catch(view_bp)
@sessionmaker
def download_timetable(db):

    '''Загрузка расписания за определенным днем недели'''

    weekday_num = session['weekday_num']
    weekday = Weekday(weekday_num)

    user_uid = current_user.id
    tutors, students = get_persons(user_uid, db)

    lessons = query_lessons(tutors, weekday_num, db)

    timetable = Timetable(lessons, students)
    timetable_excel = timetable.excel()

    return send_file(timetable_excel, download_name=f"Расписание ({weekday.label.lower()}).xlsx", as_attachment=True)

@view_bp.route('/change_name', methods=['POST'])
@login_required
@error_catch(view_bp)
@client_data_catch
@sessionmaker
def change_name(client_data, db):

    '''Изменение имени ученика или тьютора'''

    person_data = persons_dict[client_data['person_type']]
    person = person_data['getter'](client_data['person_id'], db)
    setattr(person, person_data['name'], client_data['name'])
    db.commit()

    return {'new_name': client_data['name'], 'person_id': client_data['person_id']}

@view_bp.route('/devision_by_zero', methods=['GET'])
@login_required
@error_catch(view_bp)
def devision_by_zero():
    '''
    Возвращает деление на 0
    для возбуждения исключения
    Проверка работы декоратора - перехватчика ошибок
    '''
    return 0 / 0