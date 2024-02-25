
from functools import wraps

def error_catch(blueprint=None):

  '''
  Декоратор-перехватчик ошибок
  В случае, если функция выполнена с ошибкой,
  возвращает словарь с информацией об ошибке
  '''

  def error_catch_body(func):

    func_name = f'{blueprint.name}.{func.__name__}' if blueprint else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
      try:
        return func(*args, **kwargs)

      except Exception as e:
        print(e)

        return {
            'error': True,
            'error_human_text': 'При выполнении функции произошла критическая ошибка',
            'func_name': func_name,
            'error_text': str(e),
            'error_banner': 'Критическая ошибка!'
        }
      
    return wrapper
  
  return error_catch_body
