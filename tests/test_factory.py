from fai import create_app

def test_config():
    assert not create_app().testing
    app = create_app()
    app.config['TESTING']=True
    assert app.testing