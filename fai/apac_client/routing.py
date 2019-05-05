from flask import (current_app, Blueprint, render_template)
from fai.apac_client.forms import ApaczkaPlaceOrderRequestForm
from fai.fakt_client import getinvoicebyid
from fai.apac_client.apac_client import ApaClient

apac = Blueprint('apac', __name__)

apaclient = ApaClient()

@apac.route("/placeorderform/<id>", methods=['GET','POST'])
def placeorderform(id: str):
    form = ApaczkaPlaceOrderRequestForm()
    if form.validate_on_submit():
        #TODO
        try:
            apaclient.sendOrderRequest(form=form)
        except Exception:
            print(Exception)
    invoice = getinvoicebyid(id=id)
    return render_template(template_name_or_list='apacplaceorderform.html', form=form, invoice=invoice)



