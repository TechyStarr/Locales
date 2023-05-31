from flask import Flask, request, session, Blueprint, render_template, redirect, url_for, flash
from http import HTTPStatus
# from ...api.models.users import User
from flask_caching import Cache
from flask_login import login_user, logout_user, current_user, login_required
from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash



auth = Blueprint('User', __name__, url_prefix='/auth')


@auth.route('/signup', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')