import pytest
from fai import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    # app.config['FAI_USER'] = 'test'
    # app.config['FAI_USER_PASS'] = '$2b$12$t4WTEyHpMjH98jTR441KhuSkK.g9832NU.BLXYNZVagWUM/D31NSa'
    yield app


'''
source venv/bin/activate
export FLASK_ENV=development
export FLASK_DEBUG=True
export FLASK_SECRET_KEY=494b1e6a62e2fbf3663265324c0a12a521df9dbc7ab70bde9b9c511b3d6a6a66
export FAKT_DOMAIN=vp885
export FAKT_TOKEN=qzuikLUGgI42y6yVS59/vp885
export APAC_API_KEY=Apaczka2019
export APAC_LOGIN=biuro@viti.com.pl
export APAC_PASS=VIti1234
export APAC_WSDL=https://www.apaczka.pl/webservice/order/?wsdl
export FAI_USER=admin1
export FAI_USER_PASS='$2b$12$OSa5/UxaG/lujCKhWvYUSuq.O/ggl4G9icoGAbgtvPAet/ow0n2Sy'
'''


@pytest.fixture()
def client(app):
    return app.test_client()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
