from fai.config import FaiConfig as config
from fai import countries
from fai.exceptions import ApacAuthenticationException

from suds.client import Client

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
        placeOrderRequest = self.client.factory.create('ns0:PlaceOrderRequest')
        order = self.client.factory.create('ns0:Order')
        placeOrderRequest.authorization = self.auth

        order.accountNumber = form.accountNumber.data
        order.contents = form.contents.data
        order.isDomestic = str(form.isDomestic.data).lower()

        order.notificationDelivered.isReceiverEmail = str(form.notificationDelivered_isReceiverEmail.data).lower()
        order.notificationDelivered.isReceiverSms = str(form.notificationDelivered_isReceiverSms.data).lower()
        order.notificationDelivered.isSenderEmail = str(form.notificationDelivered_isSenderEmail.data).lower()
        order.notificationDelivered.isSenderSms = str(form.notificationDelivered_isSenderSms.data).lower()

        order.notificationException.isReceiverEmail = str(form.notificationException_isReceiverEmail.data).lower()
        order.notificationException.isReceiverSms = str(form.notificationException_isReceiverSms.data).lower()
        order.notificationException.isSenderEmail = str(form.notificationException_isSenderEmail.data).lower()
        order.notificationException.isSenderSms = str(form.notificationException_isSenderSms.data).lower()

        order.notificationNew.isReceiverEmail = str(form.notificationNew_isReceiverEmail.data).lower()
        order.notificationNew.isReceiverSms = str(form.notificationNew_isReceiverSms.data).lower()
        order.notificationNew.isSenderEmail = str(form.notificationNew_isSenderEmail.data).lower()
        order.notificationNew.isSenderSms = str(form.notificationNew_isSenderSms.data).lower()

        order.notificationSent.isReceiverEmail = str(form.notificationSent_isReceiverEmail.data).lower()
        order.notificationSent.isReceiverSms = str(form.notificationSent_isReceiverSms.data).lower()
        order.notificationSent.isSenderEmail = str(form.notificationSent_isSenderEmail.data).lower()
        order.notificationSent.isSenderSms = str(form.notificationSent_isSenderSms.data).lower()

        order.options = form.options.data
        order.orderPickupType = form.orderPickupType.data
        order.pickupDate = form.pickupDate.data
        order.pickupTimeFrom = form.pickupTimeFrom.data
        order.pickupTimeTo = form.pickupTimeTo.data

        order.receiver.addressLine1 = form.receiver_addressLine1.data
        order.receiver.addressLine2 = form.receiver_addressLine2.data
        order.receiver.city = form.receiver_city.data
        order.receiver.contactName = form.receiver_contactName.data
        order.receiver.countryId = form.receiver_countryId.data
        order.receiver.email = form.receiver_email.data
        order.receiver.name = form.receiver_name.data
        order.receiver.phone = form.receiver_phone.data
        order.receiver.postalCode = form.receiver_postalCode.data

        order.referenceNumber = form.referenceNumber.data

        order.sender.addressLine1 = form.sender_addressLine1.data
        order.sender.addressLine2 = form.sender_addressLine2.data
        order.sender.city = form.sender_city.data
        order.sender.contactName = form.sender_contactName.data
        order.sender.countryId = form.sender_countryId.data
        order.sender.email = form.sender_email.data
        order.sender.name = form.sender_name.data
        order.sender.phone = form.sender_phone.data
        order.sender.postalCode = form.sender_postalCode.data

        order.serviceCode = form.serviceCode.data

        shipment = self.client.factory.create('ns0:Shipment')
        #
        # shipment.dimension1 = Decimal(form.shipment_dimension1.data)/1
        # shipment.dimension2 = Decimal(form.shipment_dimension2.data)/1
        # shipment.dimension3 = Decimal(form.shipment_dimension3.data)/1

        shipment.dimension1 = 20
        shipment.dimension2 = 30
        shipment.dimension3 = 15

        # shipment.options = form.shipment_options.data
        shipment.options = None
        # shipment.position = Decimal(form.shipment_position.data)
        shipment.position = 0
        # shipment.shipmentTypeCode = form.shipmentTypeCode.data
        shipment.shipmentTypeCode = 'PACZ'
        # shipment.shipmentValue = Decimal(form.shipmentValue.data)
        shipment.weight = 1

        order.shipments = []
        order.shipments.append(shipment)

        placeOrderRequest.order = order

        placeOrderRequest.authorization.apiKey = 'Apaczka2019'
        placeOrderRequest.authorization.login = 'biuro@viti.com.pl'
        placeOrderRequest.authorization.password = 'VIti1234'

        print(placeOrderRequest)

        response = self.client.service.placeOrder(placeOrderRequest)
        print(response)

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

# client = ApaClient()
# print(client)
#
# soapclient = client.client
# print(soapclient)
#
# auth = soapclient.factory.create('ns0:Authorization')
# auth.apiKey = 'Apaczka2019'
# auth.login = 'biuro@viti.com.pl'
# auth.password ='VIti1234'
#
# placeOrderRequest = soapclient.factory.create('ns0:PlaceOrderRequest')
# placeOrderRequest.authorization = auth
# print(placeOrderRequest)
#
# resp = soapclient.service.placeOrder(placeOrderRequest)
# print(resp)

# shipment = client.client.factory.create('ns0:Shipment')
# print(client.client)
# # print(client.order)
# orderrequest = client.placeorderrequest()
# print(orderrequest)
# country = client.getcountry('Polska')
# print(country)
#
# # print(client)
# # countryRequest = client.factory.create('ns0:CountryRequest')
# # auth = client.factory.create('ns0:Authorization')
# # auth.apiKey = f'{conf.apacapikey}'
# # auth.login = f'{conf.apaclogin}'
# # auth.password = f'{conf.apacpassword}'
# # countryRequest.authorization = auth
# #
# #
# # print(countryRequest)
#
#
# #
# #
# # auth_response = client.service.validateAuthData(auth)
# # count_response = client.service.getCountries(countryRequest)
# # print(auth_response)
# # print(count_response)
# print('END')
