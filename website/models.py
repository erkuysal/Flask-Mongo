# Package imports
# from pymongo import MongoClient
from datetime import datetime, UTC
from flask_login import UserMixin

# relative imports
# ...
from . import dbase

# additional imports
import bcrypt


# --------------------------- User Model -----------------------------------


class User(UserMixin, dbase.Document):
    email = dbase.EmailField(unique=True, required=True)
    username = dbase.StringField(unique=True, required=True)
    password = dbase.StringField(required=True)
    created_at = dbase.DateTimeField(default=datetime.now(UTC))  # utc to keep it universal

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def check_password(self, password):
        return bcrypt.checkpw(self.password.encode(), password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# Post model --------------------------------------------------------------

