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
        return 'mrcn hello test 1'

    return app


app = create_app()
app.run()