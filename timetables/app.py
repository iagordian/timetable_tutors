from flask import Flask, send_from_directory, request, render_template, g, session, redirect, url_for, jsonify, flash
from flask_login import LoginManager, login_user, logout_user, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
from auth import UserLogin
from data_base import sessionmaker

SECRET_KEY = '2b33e737f8c95f06a4043c45a1cac30712c3d1ed'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager(app)
login_manager.login_view = "auth_bp.login"

@login_manager.user_loader
def load_user(user_id):
    return UserLogin().fromDB(user_id)

from auth import auth_bp, auth
app.register_blueprint(auth_bp)

from error import error_bp
app.register_blueprint(error_bp)

from js_scripts import scripts_bp
app.register_blueprint(scripts_bp)

from timetable import timetable_bp
app.register_blueprint(timetable_bp)

from help import help_bp
app.register_blueprint(help_bp)

from view import view_bp, view
app.register_blueprint(view_bp)

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000)