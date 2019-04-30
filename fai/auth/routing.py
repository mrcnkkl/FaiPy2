from flask import (current_app, Blueprint, render_template, flash, redirect, url_for)
from fai.auth.forms import LoginForm
from fai import bcrypt
import os

authbp = Blueprint('login', __name__)


@authbp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == os.getenv('FAI_USER') \
                and bcrypt.check_password_hash('$2b$12$OSa5/UxaG/lujCKhWvYUSuq.O/ggl4G9icoGAbgtvPAet/ow0n2Sy', form.password.data):
            flash('Jesteś zalogowany', 'success')
            return redirect(url_for('home.home'))
        else:
            flash('Nieprawidłowe hasło i/lub login', 'danger')
            return redirect(url_for('login.login'))
    return render_template('login.html', form=form)
