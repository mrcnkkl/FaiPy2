from fai import create_app
from flask import current_app


def test_config():
    assert not create_app().testing
    app = create_app()
    app.config['TESTING'] = True
    assert app.testing
    assert current_app is not None


def test_app_is_development(app):
    assert app.config['SECRET_KEY'] == 'secretkey'
    assert app.config['TESTING'] == True
    assert app.config['DEBUG'] == True
