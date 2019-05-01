from flask import (Blueprint, render_template, flash, redirect, url_for, request,session, abort)
from flask_login import login_user, current_user, logout_user, login_required
from fai.auth.forms import LoginForm
from fai import bcrypt
import os, datetime
from fai.auth.user import User

authbp = Blueprint('login', __name__)


@authbp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.home'))
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == os.getenv('FAI_USER') \
                and bcrypt.check_password_hash('$2b$12$OSa5/UxaG/lujCKhWvYUSuq.O/ggl4G9icoGAbgtvPAet/ow0n2Sy', form.password.data):
            user = User()
            login_user(user, duration=datetime.timedelta(seconds=5))#, remember=True)
            flash('Jesteś zalogowany', 'success')
            next = request.args.get('next')
            if next is not None:
                return abort(400)
            return redirect(url_for('home.home'))
        else:
            flash('Nieprawidłowe hasło i/lub login', 'danger')
            return redirect(url_for('login.login'))
    return render_template('login.html', form=form)


@authbp.route('/login', methods=['GET'])
@login_required
def logout():
    current_user.is_authenticated = False
    logout_user()
    x = session
    print(x)
    form = LoginForm()
    return redirect('login')

