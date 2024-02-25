
from flask import Blueprint

view_bp = Blueprint('view_bp', __name__, template_folder='templates', static_folder='static', url_prefix='/')