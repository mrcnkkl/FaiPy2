import pytest
from flask import session, g

def test_loginform(client):
    response = client.get('/login')
    assert response

def test_login(client, auth):
    assert client.get('/login').status_code == 200
    assert auth.login().status_code == 200

    with client:
        response = client.get('/home')
        assert  response.status_code == 302
