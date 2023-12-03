from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

bootstrap = Bootstrap5()

login_manager = LoginManager()
login_manager.login_view = "auth.login"

db = MongoEngine()


def create_app():
    app = Flask(__name__, template_folder='templates')

    # Initialisations
    # ...
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    # Configurations
    # ...
    app.config['SECRET_KEY'] = 'notfoundablesecretkey'
    app.config["MONGODB_SETTINGS"] = [
        {
            "db": "profiles",
            "host": "localhost",
            "port": 27017,
            "alias": "default",
        }]


    # Blueprint imports
    # ...
    from .blueprints.main import main
    from .blueprints.auth import auth

    # Blueprint registers
    # ...
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Model imports
    # ...
    from .models import User, Post

    return app
