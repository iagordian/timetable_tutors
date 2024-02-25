
from flask import Blueprint

timetable_bp = Blueprint('timetable_bp', __name__, template_folder='templates', static_folder='static', url_prefix='/timetable')

from timetable.timetable_obj import Timetable