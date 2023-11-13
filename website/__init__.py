from flask import Flask
from flask_bootstrap import Bootstrap5

bootstrap = Bootstrap5()


def create_app():
    app = Flask(__name__, template_folder='templates')

    # Initialisations
    # ...
    bootstrap.init_app(app)

    # Configurations
    # ...
    app.config['SECRET_KEY'] = 'notfoundablesecretkey'

    # Blueprint imports
    # ...
    from .views import views
    from .blueprints.auth import auth

    # Blueprint registers
    # ...
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
