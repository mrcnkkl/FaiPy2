from fai.auth.routing import login

def test_loginform(client):
    response = client.get('/login')
    assert response

