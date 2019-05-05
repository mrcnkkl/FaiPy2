from flask import (current_app, Blueprint, render_template)
from flask_login import login_required
from fai.fakt_client import getinvoicebyid, getinvoicelistofperiod

inv = Blueprint('inv', __name__)

@inv.route('/invoices')
@login_required
def invoices(period):
    try:
        invoices = getinvoicelistofperiod(period)
    except:
        #TODO
        print('_________________________')
    return render_template('invoices.html', invoices = invoices)


@inv.route("/invoices/<id>")
@login_required
def invoice(id: str):
    invoice = getinvoicebyid(id=id)
    return render_template(template_name_or_list='invoice.html', invoice=invoice)

