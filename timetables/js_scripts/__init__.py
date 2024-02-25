
from flask import Blueprint

scripts_bp = Blueprint('scripts_bp', __name__, template_folder='templates', static_folder='static', url_prefix='/js')