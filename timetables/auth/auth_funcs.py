
from collections import namedtuple
from werkzeug.security import check_password_hash
from models import User
from sqlalchemy.orm import Session

User_Check = namedtuple('User_Check', ['login', 'password', 'user_id'], defaults=[False, False, None])


def check_authorization(login: str, password: str, db: Session) -> User_Check:

    '''
    Проверка данных авторизации
    Возвращает объект с данными
    об ошибках авторизации
    '''

    user = db.query(User).filter_by(login=login).first()
    if not user:
        return User_Check()

    if not check_password_hash(user.password_hash, password):
        return User_Check(True)

    return User_Check(True, True, user.id)