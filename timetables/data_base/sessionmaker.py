
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from functools import wraps

SQLALCHEMY_DATABASE_URL = 'sqlite:///istanse/data_base.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    '''
    Возвращает объект сессии
    '''
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

def sessionmaker(func):

    '''
    Декоратор, который передает функции в
    качестве аргумента объект сессии работы с БД
    Делает коммит в случае успеха функции или rollback
    в случае, если функция была выполнена с исключением
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):

        db = get_db()

        try:
            result = func(*args, db=db, **kwargs)
            db.commit()
            return result
        except Exception as e:
            db.rollback()

            '''
            Реализовывает ошибку, чтобы она была перехвачена декоратором-перехватчиком ошибок
            '''
            raise e

    return wrapper