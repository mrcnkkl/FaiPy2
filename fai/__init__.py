import os
from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.getenv('FLASK_SECRET_KEY', default=None),
        # SECRET_KEY='secret',
        FLASK_ENV = os.getenv('FLASK_ENV', default='production')
    )

    @app.route('/test')
    def test():
        return '<h2>MRCN - deployed to heroku + {var}</h2>'.format(var=os.getenv('MRCN_TEST'))

    from fai.main.routing import homebp
    from fai.auth.routing import authbp
    app.register_blueprint(homebp)
    app.register_blueprint(authbp)

    return app