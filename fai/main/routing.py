from flask import (current_app, Blueprint, render_template)
from flask_login import login_required
from fai.main.forms import FaktInvPeriodSmallForm
from fai.fakt_client.routing import invoices

homebp = Blueprint('home', __name__)

@homebp.route('/', methods=['GET', 'POST'])
@homebp.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    form = FaktInvPeriodSmallForm()
    if form.validate_on_submit():
        return invoices(form.period.data)
    return render_template('home.html', form=form)
