
from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates', static_folder='static', url_prefix='/auth')

from auth.auth_funcs import check_authorization
from auth.user_login import UserLogin