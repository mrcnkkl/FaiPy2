from flask import (current_app, Blueprint, render_template, flash, redirect, url_for)
from flask_login import UserMixin, login_user
from fai.auth.forms import LoginForm
from fai import bcrypt, login_manager
import os

authbp = Blueprint('login', __name__)


@authbp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == os.getenv('FAI_USER') \
                and bcrypt.check_password_hash('$2b$12$OSa5/UxaG/lujCKhWvYUSuq.O/ggl4G9icoGAbgtvPAet/ow0n2Sy', form.password.data):
            user = User('user')
            login_user(user)
            flash('Jesteś zalogowany', 'success')
            return redirect(url_for('home.home'))
        else:
            flash('Nieprawidłowe hasło i/lub login', 'danger')
            return redirect(url_for('login.login'))
    return render_template('login.html', form=form)


class User(UserMixin):

    def __init__(self, role, id=0):
        super().__init__()
        self.role = role
        self.id = id

    def get_id(self):
        return super().get_id()
