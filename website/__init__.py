from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

from os import path

current_dir = path.abspath(path.dirname(__file__))
base_dir = path.dirname(current_dir)

config_path = path.join(base_dir, 'config.py')


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
    app.config.from_pyfile(config_path)
    # # ...
    # # File/Upload Configurations
    # app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    # app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
    # app.config['UPLOAD_PATH'] = 'uploads'
    #
    # # Database Configurations
    # app.config['SECRET_KEY'] = 'notfoundablesecretkey'
    # app.config["MONGODB_SETTINGS"] = [
    #     {
    #         "db": "profiles",
    #         "host": "localhost",
    #         "port": 27017,
    #         "alias": "default",
    #     }]

    # Blueprint imports
    # ...
    from .blueprints.main import main
    from .blueprints.auth import auth
    from .blueprints.actions import act

    # Blueprint registers
    # ...
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(act, url_prefix='/')

    # Model imports
    # ...
    from .models import User, Post

    return app
