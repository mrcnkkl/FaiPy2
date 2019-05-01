import os, datetime
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login.login'
login_manager.login_message_category = 'secondary'
login_manager.login_message = 'Zaloguj się aby przejść dalej'
from fai.auth.user import User



def create_app(config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.getenv('FLASK_SECRET_KEY', default=None),
        PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=60),
        # SECRET_KEY='secret',
        FLASK_ENV=os.getenv('FLASK_ENV', default='production')
    )


    login_manager.init_app(app)

    print(login_manager)

    @login_manager.user_loader
    def load_user(user_id):
        return User()

    @app.route('/test')
    def test():
        return '<h2>MRCN - deployed to heroku + {var}</h2>'.format(var=os.getenv('MRCN_TEST'))

    from fai.main.routing import homebp
    from fai.auth.routing import authbp
    app.register_blueprint(homebp)
    app.register_blueprint(authbp)

    return app
