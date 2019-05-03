from flask import (current_app, Blueprint, render_template)
from fai.apac_client.forms import ApaczkaPlaceOrderRequestForm

apac = Blueprint('apac', __name__)


@apac.route("/placeorderform/<id>", methods=['GET','POST'])
def placeorderform(id: str):
    form = ApaczkaPlaceOrderRequestForm()
    # if form.validate_on_submit():
    #     # print('if form.validate_on_submit():')
    #     apaclient.sendOrderRequest(form=form)
    # invoice = faktclient.getinvoicebyid(id=id)
    return render_template(template_name_or_list='apacplaceorderform.html', form=form, invoice=None)#invoice)





# @inv.route('/invoices')
# @login_required
# def invoices(period):
#     try:
#         invoices = getinvoicelistofperiod(period)
#     except:
#         #TODO
#         print('_________________________')
#     return render_template('invoices.html', invoices = invoices)
#
#
# @inv.route("/invoices/<id>")
# @login_required
# def invoice(id: str):
#     invoice = getinvoicebyid(id=id)
#     return render_template(template_name_or_list='invoice.html', invoice=invoice)

