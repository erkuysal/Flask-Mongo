import os
_basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    DATABASE_CONNECT_OPTIONS = {}

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection against *Cross-site Request Forgery (CSRF)*
    WTF_CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY')

    PATHS = {
        'Uploads': 'uploads',
        'Downloads': 'downloads'
    }

    SETTINGS = {
        'MaxFileSize': '1024',
        'LogLevel': 'info'
    }

    # Secret key for signing cookies
    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'SECRET'

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    """Statement for enabling the development environment"""
    # Define the database - we are working with
    MONGODB_SETTINGS = {
        "db": "profiles",
        "host": "localhost",
        "port": 27017,
        "alias": "default",
    }
    DEBUG = True


class APIConfig(Config):
    """Statement for enabling the api environment"""
    # Define the database - we are working with
    MONGODB_SETTINGS = {
        "db": "profiles",
        "host": "localhost",
        "port": 27017,
        "alias": "default",
    }
    WTF_CSRF_ENABLED = False


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    MONGODB_SETTINGS = {
        "db": "profiles",
        "host": "localhost",
        "port": 27017,
        "alias": "default",
    }


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'api': APIConfig,
}











