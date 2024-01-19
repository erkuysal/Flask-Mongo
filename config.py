import os

import imghdr

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


SECRET_KEY = 'definitely-not-foundable-key'
SESSION_TYPE = 'mongodb'

# MongoDB configuration
MONGODB_SETTINGS = [
    {
        "db": "profiles",
        "host": "localhost",
        "port": 27017,
        "alias": "default",
    }]

# File/Upload Configurations
MAX_CONTENT_LENGTH = 2 * 1024 * 1024
UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
UPLOAD_PATH = 'uploads'

@staticmethod
def init_app(app):
    pass
