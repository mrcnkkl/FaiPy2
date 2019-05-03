import os


class FaiConfig:
    flask_env = os.getenv('FLASK_ENV')
    flask_debug = os.getenv('FLASK_DEBUG')
    flask_secret_key = os.getenv('FLASK_SECRET_KEY')
    fakt_domain = os.getenv('FAKT_DOMAIN')
    fakt_token = os.getenv('FAKT_TOKEN')
    apac_api_key = os.getenv('APAC_API_KEY')
    apac_login = os.getenv('APAC_LOGIN')
    apac_pass = os.getenv('APAC_PASS')
    apac_wsdl = 'https://www.apaczka.pl/webservice/order/?wsdl'
    fai_user = os.getenv('FAI_USER')
    fai_user_pass = os.getenv('FAI_USER_PASS')


