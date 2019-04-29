from flask import (current_app, Blueprint, render_template)

homebp = Blueprint('home', __name__)

@homebp.route('/')
@homebp.route('/home')
def home():
    return render_template('home.html', form=None)