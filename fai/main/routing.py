from flask import (current_app, Blueprint, render_template)
from flask_login import login_required

homebp = Blueprint('home', __name__)

@homebp.route('/')
@homebp.route('/home')
@login_required
def home():
    return render_template('home.html', form=None)