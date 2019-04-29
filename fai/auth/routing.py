from flask import (current_app, Blueprint, render_template, flash, redirect, url_for)
from fai.auth.forms import LoginForm

authbp = Blueprint('login', __name__)

@authbp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Jesteś zalogowany', 'success')
        return redirect(url_for('home.home'))
    return render_template('login.html', form=form)