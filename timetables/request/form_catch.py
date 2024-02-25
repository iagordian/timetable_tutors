
from flask import request
from functools import wraps

def client_data_catch(func):

    '''
    Декоратор преобразует параметры request в словарь,
    который декорируемая функция принимает в качестве аргумента
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        request_method = request.method.upper()

        if request_method == 'GET':
            client_data = dict(request.args)

        if request_method == 'POST':
            client_data = dict(request.form)

        for k, v in client_data.items():
            if v.isdigit():
                client_data[k] = int(v)
            if v == 'None':
                client_data[k] = None

        return func(*args, client_data=client_data, **kwargs)

    return wrapper