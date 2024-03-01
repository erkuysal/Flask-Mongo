from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_mongoengine import MongoEngine
from flask_login import LoginManager


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
    app.config['SECRET_KEY'] = 'RandomSecretKey'
    app.config['FLASK_DEBUG'] = True
    app.config['MONGODB_SETTINGS'] = {
        "db": "profiles",
        "host": "localhost",
        "port": 27017,
        "alias": "default",
    }

    app.config['UPLOAD_FOLDER'] = {
        'Uploads': 'uploads'
    }

    app.config['DOWNLOAD_FOLDER'] = {
        'Downloads': 'downloads'
    }

    app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1 MB

    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']

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
