import pytest
from fai import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING']=True
    yield app

