# imports


class Config(object):
    SECRET_KEY = 'definitely-not-foundable-key'
    SESSION_TYPE = 'mongodb'

    # MongoDB configuration
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/profiles'

    # Session configuration
    app.config['SESSION_TYPE'] = 'mongodb'
    app.config['SESSION_PERMANENT'] = False  # You can set this to True if you want permanent sessions
    app.config['SESSION_USE_SIGNER'] = True  # Enable session id signing for security
    app.config['SESSION_KEY_PREFIX'] = 'profile_'  # A prefix for session keys
