
from datetime import date
from typing import Optional

class Weekday:

  '''
  Описание дня недели
  При инциализации принимает номер или
  определяет сегодняшний день недели при помощи
  модуля datetime
  '''

  lables = {
      1: 'Понедельник',
      2: 'Вторник',
      3: 'Среда',
      4: 'Четверг',
      5: 'Пятница',
  }

  def __init__(self, weekday_num: Optional[int]=None):
    self.weekday_num = weekday_num

  def __call__(self):
    '''
    Возвращает номер дня недели
    В субботу или воскресенье возвращает понедельник
    '''
    return self.weekday_num if self.weekday_num < 6 else 1

  @property
  def label(self):
    return self.lables[self.__call__()]

  @property
  def weekday_num(self):
      return self._weekday_num if self._weekday_num < 6 else 1

  @weekday_num.setter
  def weekday_num(self, weekday_num: Optional[int]=None):
      if type(weekday_num) == str:
          if weekday_num.isdigit():
              weekday_num = int(weekday_num)
      assert weekday_num in [1, 2, 3, 4, 5, None]
      self._weekday_num = weekday_num or date.today().weekday() + 1

  def __repr__(self):
    return self.label