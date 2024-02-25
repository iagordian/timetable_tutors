
from flask import Blueprint

error_bp = Blueprint('error_bp', __name__, template_folder='templates', static_folder='static', url_prefix='/error')

from error.error_catch import error_catch

