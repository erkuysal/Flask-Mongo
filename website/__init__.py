from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager

bootstrap = Bootstrap5()
login_manager = LoginManager()

login_manager.login_view = "auth.login"


def create_app():
    app = Flask(__name__, template_folder='templates')

    # Initialisations
    # ...
    bootstrap.init_app(app)
    login_manager.init_app(app)

    # Configurations
    # ...
    app.config['SECRET_KEY'] = 'notfoundablesecretkey'

    # Blueprint imports
    # ...
    from .blueprints.main import main
    from .blueprints.auth import auth

    # Blueprint registers
    # ...
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
