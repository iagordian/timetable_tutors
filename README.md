# timetable_tutors
Реальный проект, использущийся в работе общеобразовательной школы. Выложен на Git для демонстрации профессиональных навыков
Приложение было написано при помощи фреймворка Flask. Регистрация пользователей осуществлена при помощи модуля Flask-Login. 
Приложение выполнено в соответствии с принципами ООП, расписание, с которым взаимодействует пользователь, является написанным классом. 
В приложении используется декоратор-перехватчик ошибок, который обнаруживает происходящие исключения и возвращает их пользователю в качестве сообщения об ошибке. 
Во время разработки приложения активно использовались модули functools и collections FrontEnd часть приложения разработана при помощи JQuery

Краткое изложение структуры класса Timetable

# Ячейка расписания
class TM_Ceil:
  def __init__(self, val: Optional[uuid.UUID]=None, label: str=''):
    self.val = val
    self.label = label

@total_ordering
class TM_Row:

  def __init__(self, tutor_id: Optional[uuid.UUID], tutor_name: str, lessons: Query):
    self.tutor_id = tutor_id
    self.tutor_name = tutor_name
    self.cursor = 1

    # Структура defaultdict позволяет создать ячейку "поумолчанию", пустую
    self.lessons = defaultdict(lambda: TM_Ceil())

    if lessons:
      for lesson in lessons:
        self.lessons[lesson.lesson_num] = TM_Ceil(lesson.student_id, lesson.student.student_name)

  def __iter__(self):
    return self

  def __next__(self):

    '''Объект позволяет итерироваться по собственным ячейкам'''

    if self.cursor > 8:
      raise StopIteration

    lesson = self.lessons[self.cursor]
    self.cursor += 1
    return lesson

class Timetable:

  def __init__(self, lessons: List[dict], students: Query):

    self.rows = []
    for tutor_lessons in lessons:
      self.rows.append(TM_Row(tutor_lessons['tutor'].tutor_id,
                              tutor_lessons['tutor'].tutor_name,
                              lessons = tutor_lessons['lessons']))

    self.options = {student.student_id: student.student_name for student in students if student.active}
    self.options[None] = ''

    self.iteration_size = len(self.rows) - 1
    self.cursor = 0

    self.sort()

  def __iter__(self):
    return self

  def __next__(self):

    '''Объект позволяет итерироваться по собственным строкам'''

    if self.cursor > self.iteration_size:
      raise StopIteration

    row = self.rows[self.cursor]
    self.cursor += 1
    return row
