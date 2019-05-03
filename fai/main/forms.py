from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField, SelectMultipleField, DateField, DateTimeField
from wtforms.validators import DataRequired, Length


class FaktInvPeriodSmallForm(FlaskForm):
    period = SelectField('Wyświetl faktury z: ',
                         choices=[
                             ('last_12_months', 'Ostatnie 12 miesięcy'),
                             ('this_month', 'Ten miesiąc'),
                             ('last_30_days', 'Ostatnie 30 dni'),
                             ('last_month', 'Poprzedni miesiąc'),
                             ('this_year', 'Ten rok'),
                             ('last_year', 'Poprzedni rok'),
                             ('all', 'Wszystkie faktury')
                         ])
    submit = SubmitField('Pokaż')
