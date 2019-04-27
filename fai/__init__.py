import os
from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.getenv('FLASK_SECRET_KEY', default=None)
    )

    return app
