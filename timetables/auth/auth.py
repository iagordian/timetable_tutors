
from auth import auth_bp
from flask import render_template, flash, session, url_for, redirect
from flask_login import login_user, logout_user
from auth.user_login import UserLogin
from auth.auth_funcs import check_authorization
from request import client_data_catch
from data_base import sessionmaker
from typing import Dict


@auth_bp.route('/login', methods=['GET'])
def login():
    '''Возвращает страницу авторизации'''
    session.pop('_flashes', None)
    return render_template('/auth/auth.html')

@auth_bp.route('/logout', methods=['GET'])
def logout():
     '''Выход пользователя из системы'''
     logout_user()
     return redirect(url_for('auth_bp.login'))

@auth_bp.route('/auth', methods=['GET', 'POST'])
@client_data_catch
@sessionmaker
def authorization(client_data: Dict[str, str], db):
    '''
    Проверка данных авторизации
    В случае ошибки возвращает сообщения об авторизации,
    в противном случае авторизирует пользователя и перенаправляет
    на главную страницу приложения
    '''

    check_result = check_authorization(client_data['login'], client_data['password'], db)

    if not check_result.login:
        flash('Введенного логина не существует в системе')

    elif not check_result.password:
        flash('Введенный пароль не соответсвует паролю пользователя')

    elif check_result.user_id:
        userlogin = UserLogin().create(check_result.user_id)
        login_user(userlogin)
        return redirect(url_for('view_bp.index'))


    return render_template('/auth/auth.html')

