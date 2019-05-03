from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField, SelectMultipleField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length


class ApaczkaPlaceOrderRequestForm(FlaskForm):
    accountNumber = StringField(label='Nr konta dla przesyłek pobraniowych',
                                description='Nr konta dla przesyłek pobraniowych. Wymagane,gdy podano opcję POBRANIE.',
                                default='')
    contents = StringField(label='Zawartość przesyłki', description='Zawartość przesyłki',
                           validators=[DataRequired('To pole jest obowiązkowe'), Length(max=35)],
                           default='Siłownik hydrauliczny + osprzęt')
    isDomestic = BooleanField(label='Czy przesyłka krajowa?', description='Czy przesyłka krajowa?', default=True)

    notificationDelivered_isReceiverEmail = BooleanField(
        label='Czy wysyłać email do adresata przesyłki po zmianie statusu na dostarczoną?', default=False)
    notificationDelivered_isReceiverSms = BooleanField(
        label='Czy wysyłać sms do adresata przesyłki po zmianie statusu na dostarczoną?', default=False)
    notificationDelivered_isSenderEmail = BooleanField(
        label='Czy wysyłać email do nadawcy przesyłki po zmianie statusu na dostarczoną?', default=False)
    notificationDelivered_isSenderSms = BooleanField(
        label='Czy wysyłać SMS do nadawcy przesyłki po zmianie statusu na dostarczoną?', default=False)

    notificationException_isReceiverEmail = BooleanField(
        label='Czy wysyłać email do adresata przesyłki po zmianie statusu na wyjątek?', default=False)
    notificationException_isReceiverSms = BooleanField(
        label='Czy wysyłać sms do adresata przesyłki po zmianie statusu na wyjątek?', default=False)
    notificationException_isSenderEmail = BooleanField(
        label='Czy wysyłać email do nadawcy przesyłki po zmianie statusu na wyjątek?', default=False)
    notificationException_isSenderSms = BooleanField(
        label='Czy wysyłać email do nadawcy przesyłki po zmianie statusu na wyjątek?', default=False)

    notificationNew_isReceiverEmail = BooleanField(
        label='Czy wysyłać email do adresata przesyłki po zmianie statusu na utworzoną?', default=False)
    notificationNew_isReceiverSms = BooleanField(
        label='Czy wysyłać sms do adresata przesyłki po zmianie statusu na utworzoną?', default=False)
    notificationNew_isSenderEmail = BooleanField(
        label='Czy wysyłać email do nadawcy przesyłki po zmianie statusu na utworzoną?', default=False)
    notificationNew_isSenderSms = BooleanField(
        label='Czy wysyłać sms do nadawcy przesyłki po zmianie statusu na wysłaną?', default=False)

    notificationSent_isReceiverEmail = BooleanField(
        label='Czy wysyłać email do adresata przesyłki po zmianie statusu na wysłaną?', default=False)
    notificationSent_isReceiverSms = BooleanField(
        label='Czy wysyłać sms do adresata przesyłki po zmianie statusu na wysłaną?', default=False)
    notificationSent_isSenderEmail = BooleanField(
        label='Czy wysyłać email do nadawcy przesyłki po zmianie statusu na wysłaną?', default=False)
    notificationSent_isSenderSms = BooleanField(
        label='Czy wysyłać sms do nadawcy przesyłki po zmianie statusu na wysłaną?', default=False)

    options = SelectMultipleField('Opcje zamówienia. Dopuszczalne wartości: ', choices=[('POBRANIE', 'POBRANIE'),
                                                                                        ('ZWROT_DOK',
                                                                                         'ZWROT_DOK - zwrot dokumantów'),
                                                                                        ('DOR_OSOBA_PRYW',
                                                                                         'DOR_OSOBA_PRYW - doręczenie osoba prywatna'),
                                                                                        ('DOST_SOB',
                                                                                         'DOST_SOB -dostawa w sobotę'),
                                                                                        ('PODPIS_DOROS',
                                                                                         'PODPIS_DOROS -podpis osoby dorosłej (tylko UPS)'),
                                                                                        ('POWIADOMIENIE_SMS',
                                                                                         'POWIADOMIENIE_SMS (tylko krajowe serwisy DHL, FedEx, TNT, UPS)')
                                                                                        ])

    orderPickupType = SelectField(label=
                                  'Typ odbioru przesyłki (DLA KEX Złożenie zlecenia jest zawsze równoznaczne z zamówieniem kuriera. Godziny odbioru w KEX zawsze są między 8.00, a 16.00). Dopuszczalne wartości: ',
                                  validators=[DataRequired('To pole jest obowiązkowe')],
                                  choices=[('COURIER', 'COURIER - zamówienie odbioru przesyłek'),
                                           ('SELF', 'SELF – dostarczenie samodzielnie do kuriera'),
                                           ('BOX_MACHINE', 'BOX_MACHINE – dostarczenie samodzielnie do paczkomatu')
                                           ], default='')

    pickupDate = DateField(
        label='Data odbioru przesyłki przez kuriera.Wymagane dla orderPickupType = COURIER. (FORMAT: YYYY-MM-DD)',
        format='%Y-%m-%d')

    pickupTimeFrom = StringField(
        label='Początek przedziału godzinowego, w którym kurier ma odebrać przesyłkę. Wymagane dla orderPickupType = COURIER. (FORMAT: HH:MM)',
        default='09:00')

    pickupTimeTo = StringField(
        label='Koniec przedziału godzinowego, w którym kurier ma odebrać przesyłkę. Wymagane dla orderPickupType = COURIER. (FORMAT: HH:MM)',
        default='14:00')

    receiver_addressLine1 = StringField(label='Pierwsza linia adresu',
                                        validators=[DataRequired('To pole jest obowiązkowe')])
    receiver_addressLine2 = StringField(label='Druga linia adresu', validators=[])
    receiver_city = StringField(label='Miasto', validators=[DataRequired('To pole jest obowiązkowe')])
    receiver_contactName = StringField(label='Imię i nazwisko osoby kontaktowej',
                                       validators=[DataRequired('To pole jest obowiązkowe')])
    receiver_countryId = StringField(label='Identyfikator kraju', validators=[DataRequired('To pole jest obowiązkowe')])
    receiver_email = StringField(label='Adres email', validators=[DataRequired('To pole jest obowiązkowe')])
    receiver_name = StringField(label='Nazwa odbiorcy (nazwa firmy)',
                                validators=[DataRequired('To pole jest obowiązkowe')])
    receiver_phone = StringField(label='Numer telefonu osoby kontaktowej',
                                 validators=[DataRequired('To pole jest obowiązkowe')])
    receiver_postalCode = StringField(label='Kod pocztowy', validators=[DataRequired('To pole jest obowiązkowe')])

    referenceNumber = StringField(label='Dodatkowy (np. nr zamówienia,opis faktury)',
                                  description='Dodatkowy (np. nr zamówienia,opis faktury)',
                                  default='')

    sender_addressLine1 = StringField(label='Pierwsza linia adresu',
                                      validators=[DataRequired('To pole jest obowiązkowe')], default='ul. Bławatków 4')
    sender_addressLine2 = StringField(label='Druga linia adresu', validators=[])
    sender_city = StringField(label='Miasto', validators=[DataRequired('To pole jest obowiązkowe')],
                              default='Bielsko-Biała')
    sender_contactName = StringField(label='Imię i nazwisko osoby kontaktowej',
                                     validators=[DataRequired('To pole jest obowiązkowe')], default='Rafał Plewa')
    sender_countryId = StringField(label='Identyfikator kraju', validators=[DataRequired('To pole jest obowiązkowe')],
                                   default=0)
    sender_email = StringField(label='Adres email', validators=[DataRequired('To pole jest obowiązkowe')],
                               default='biuro@viti.com.pl')
    sender_name = StringField(label='Nazwa nadawcy', validators=[DataRequired('To pole jest obowiązkowe')],
                              default='VITI ROMUALD CHOLEWIK, MARCIN KUKLA, RAFAŁ PLEWA SPÓŁKA CYWILNA')
    sender_phone = StringField(label='Numer telefonu osoby kontaktowej',
                               validators=[DataRequired('To pole jest obowiązkowe')], default='737 641 600')
    sender_postalCode = StringField(label='Kod pocztowy', validators=[DataRequired('To pole jest obowiązkowe')],
                                    default='43-300')

    serviceCode = SelectField('Kod usługi. Dopuszczalne wartości: Usługi krajowe: ', choices=[
        ('UPS_K_STANDARD', 'UPS_K_STANDARD - Ups Standard Kraj'),
        ('UPS_K_EX_SAV', 'UPS_K_EX_SAV - Ups Express Saver Kraj'),
        ('UPS_K_EX', 'UPS_K_EX - Ups Express Kraj'),
        ('UPS_K_EXP_PLUS', 'UPS_K_EXP_PLUS - Ups Express Plus Kraj'),
        ('UPS_Z_STANDARD', 'UPS_Z_STANDARD - Ups Standard Zagranica'),
        ('UPS_Z_EX_SAV', 'UPS_Z_EX_SAV - Ups Express Saver Zagranica'),
        ('UPS_Z_EX', 'UPS_Z_EX - Ups Express Zagranica'),
        ('UPS_Z_EXPEDITED', 'UPS_Z_EXPEDITED - Ups Expedited Zagranica'),
        ('DPD_CLASSIC', 'DPD_CLASSIC - Dpd Kraj'),
        ('DPD_CLASSIC_FOREIGN', 'DPD_CLASSIC_FOREIGN - Dpd Zagranica'),
        ('DHLSTD', 'DHLSTD - DHL Standard'),
        ('DHL12', 'DHL12 - DHL Express do godz. 12'),
        ('DHL09', 'DHL09 - DHL Express do godz. 9'),
        ('DHL1722', 'DHL1722 - DHL Express w godz. 17-22'),
        ('KEX_EXPRESS', 'KEX_EXPRESS - K-EX Express'),
        ('FEDEX', 'FEDEX - '),
        ('POCZTA_POLSKA_E24', 'POCZTA_POLSKA_E24 - Pocztex24'),
        ('TNT', 'TNT - TNT Kraj'),
        ('TNT_Z', 'TNT_Z - TNT Zagranica'),
        ('INPOST', 'INPOST - Inpost Kurier'),
        ('APACZKA_DE', 'APACZKA_DE - Apaczka Niemcy'),
        ('PACZKOMAT', 'PACZKOMAT - Paczkomaty'),
        ('GLS', 'GLS - GLS zagranica'),
    ])

    shipment_dimension1 = StringField(label='Długość cm.', default=30,
                                      validators=[DataRequired('To pole jest obowiązkowe')])
    shipment_dimension2 = StringField(label='Szerokość cm.', default=30,
                                      validators=[DataRequired('To pole jest obowiązkowe')])
    shipment_dimension3 = StringField(label='Wysokość cm.', default=30,
                                      validators=[DataRequired('To pole jest obowiązkowe')])

    shipment_options = SelectField(
        'Opcje przesyłki. Dla paczkomatów należy jako pierwszy parametr podać numer paczkomatu nadawcy, jako drugi parametr numer paczkomatu odbiorcy. Dopuszczalne wartości: ',
        choices=[
            ('', ''),
            ('', ''),
            ('UBEZP', 'UBEZP – dodatkowe ubezpieczenie paczki'),
            ('PRZES_NIETYP', 'PRZES_NIETYP – przesyłka nietypowa (wymaga dodatkowej obsługi)'),
            ('DUZA_PACZKA', 'DUZA_PACZKA – duża paczka (tylko dla UPS)'),
        ], default=None)

    shipment_position = StringField(label='Nr porządkowy przesyłki (liczony od 0)', default='0',
                                    validators=[DataRequired('To pole jest obowiązkowe')])

    shipmentTypeCode = SelectField(
        'Typ przesyłki. Dopuszczalne wartości: ',
        choices=[
            ('LIST', 'LIST - koperta'),
            ('PACZ', 'PACZ - paczka'),
            ('PALETA', 'PALETA - 2 wymiary stałe 120 x 80'),
        ])

    shipmentValue = StringField(
        label='Wartość przysyłki w GROSZACH (do ubezpieczenia). Wymagane, gdy podano opcję UBEZP.', default='0')

    weight = StringField(label='Waga przesyłki (w kg).', default='10',
                         validators=[DataRequired('To pole jest obowiązkowe')])

    submit = SubmitField('Wyślij')
