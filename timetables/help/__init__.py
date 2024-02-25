
from flask import Blueprint

help_bp = Blueprint('help_bp', __name__, template_folder='templates', static_folder='static', url_prefix='/help')