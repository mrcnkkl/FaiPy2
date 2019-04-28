import os
from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.getenv('FLASK_SECRET_KEY', default=None),
        FLASK_ENV = os.getenv('FLASK_ENV', default='production')
    )

    @app.route('/')
    def test():
        return '<h2>MRCN - deployed to heroku + {var}</h2>'.format(var=os.getenv('ZMIENNA'))

    return app