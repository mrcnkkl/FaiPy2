from fai.config import FaiConfig as config
from fai import countries
from fai.exceptions import ApacAuthenticationException
from suds.client import Client
import datetime


class ApaClient:

    def __init__(self):
        self.client = Client(f'{config.apac_wsdl}')
        # ------START: create and check authorisation----------------------
        self.auth = self.client.factory.create('ns0:Authorization')
        self.auth.apiKey = f'{config.apac_api_key}'
        self.auth.login = f'{config.apac_login}'
        self.auth.password = f'{config.apac_pass}'
        self._validateauthdata()
        # ------END OF: create and check authorisation----------------------

    def sendOrderRequest(self, form):
        place_order_request = self.client.factory.create('ns0:PlaceOrderRequest')
        order = self.client.factory.create('ns0:Order')
        place_order_request.authorization = self.auth

        # order.accountNumber = form.accountNumber.data
        order.codAmount = None
        order.contents = form.contents.data
        order.isDomestic = form.isDomestic.data
        order.id = None
        order.netAmount = None

        notificationDelivered = self.client.factory.create('ns0:OrderNotification')
        notificationDelivered.isReceiverEmail = str(form.notificationDelivered_isReceiverEmail.data).lower()
        notificationDelivered.isReceiverSms = str(form.notificationDelivered_isReceiverSms.data).lower()
        notificationDelivered.isSenderEmail = str(form.notificationDelivered_isSenderEmail.data).lower()
        notificationDelivered.isSenderSms = str(form.notificationDelivered_isSenderSms.data).lower()
        order.notificationDelivered = notificationDelivered

        notificationException = self.client.factory.create('ns0:OrderNotification')
        notificationException.isReceiverEmail = str(form.notificationException_isReceiverEmail.data).lower()
        notificationException.isReceiverSms = str(form.notificationException_isReceiverSms.data).lower()
        notificationException.isSenderEmail = str(form.notificationException_isSenderEmail.data).lower()
        notificationException.isSenderSms = str(form.notificationException_isSenderSms.data).lower()
        order.notificationException = notificationException

        notificationNew = self.client.factory.create('ns0:OrderNotification')
        notificationNew.isReceiverEmail = str(form.notificationNew_isReceiverEmail.data).lower()
        notificationNew.isReceiverSms = str(form.notificationNew_isReceiverSms.data).lower()
        notificationNew.isSenderEmail = str(form.notificationNew_isSenderEmail.data).lower()
        notificationNew.isSenderSms = str(form.notificationNew_isSenderSms.data).lower()
        order.notificationNew = notificationNew

        notificationSent = self.client.factory.create('ns0:OrderNotification')
        notificationSent.isReceiverEmail = str(form.notificationSent_isReceiverEmail.data).lower()
        notificationSent.isReceiverSms = str(form.notificationSent_isReceiverSms.data).lower()
        notificationSent.isSenderEmail = str(form.notificationSent_isSenderEmail.data).lower()
        notificationSent.isSenderSms = str(form.notificationSent_isSenderSms.data).lower()
        order.notificationSent.isSenderSms = notificationSent

        # options = self.client.factory.create('ns0:ArrayOfString')  # niedobowiązkowe
        # options.data = form.options.data
        # order.options = options

        order.orderPickupType = form.orderPickupType.data

        #
        # pudlist = [int(x) * 1 for x in form.pickupDate.data.split('-')]
        # order.pickupDate = datetime.datetime(*pudlist)

        # pudlist = [int(x) * 1 for x in form.pickupDate.data.split('-')]
        order.pickupDate = form.pickupDate.data

        puttlist = [int(x) * 1 for x in form.pickupTimeTo.data.split(':')]
        order.pickupTimeTo = datetime.time(*puttlist).strftime("%H:%M")

        putflist = [int(x) * 1 for x in form.pickupTimeFrom.data.split(':')]
        order.pickupTimeFrom = datetime.time(*putflist).strftime("%H:%M")

        receiver = self.client.factory.create('ns0:orderAddress')
        receiver.addressLine1 = form.receiver_addressLine1.data
        receiver.addressLine2 = form.receiver_addressLine2.data
        receiver.city = form.receiver_city.data
        receiver.contactName = form.receiver_contactName.data
        receiver.countryId = form.receiver_countryId.data
        receiver.email = form.receiver_email.data
        receiver.name = form.receiver_name.data
        receiver.phone = form.receiver_phone.data
        receiver.postalCode = form.receiver_postalCode.data
        order.receiver = receiver

        # order.referenceNumber = form.referenceNumber.data

        sender = self.client.factory.create('ns0:orderAddress')
        sender.addressLine1 = form.sender_addressLine1.data
        sender.addressLine2 = form.sender_addressLine2.data
        sender.city = form.sender_city.data
        sender.contactName = form.sender_contactName.data
        sender.countryId = form.sender_countryId.data
        sender.email = form.sender_email.data
        sender.name = form.sender_name.data
        sender.phone = form.sender_phone.data
        sender.postalCode = form.sender_postalCode.data
        order.sender = sender

        order.serviceCode = form.serviceCode.data

        shipments = self.client.factory.create('ns0:ArrayOfShipment')
        shipment = self.client.factory.create('ns0:Shipment')
        shipment_options = self.client.factory.create('ns0:ArrayOfString')

        shipment.dimension1 = form.shipment_dimension1.data
        shipment.dimension2 = form.shipment_dimension2.data
        shipment.dimension3 = form.shipment_dimension3.data

        # shipment_options = form.shipment_options.data

        shipment.options = shipment_options
        shipment.position = 0
        shipment.shipmentTypeCode = form.shipmentTypeCode.data
        shipment.shipmentValue = form.shipmentValue.data
        shipment.weight = form.weight.data
        shipments.Shipment.append(shipment)

        order.shipments = shipments


        place_order_request.order = order


        response = self.client.service.placeOrder(place_order_request)
        print(response)
        return response




    def getcountry(self, country: str):
        countdict = countries.get(country)
        country = self.client.factory.create('ns0:Country')
        country.code = countdict.get('code')
        country.id = countdict.get('id')
        country.name = countdict.get('name')
        return country

    def _validateauthdata(self):
        if not self.client.service.validateAuthData(self.auth):
            raise ApacAuthenticationException
        return True


class Authorisation:
    def __init__(self):
        pass


class OrderRequest:
    def __init__(self, auth, order):
        pass
