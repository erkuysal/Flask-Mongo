# Package imports
# from mongoengine import signals
from mongoengine import Document, EmailField, StringField, DateTimeField, ReferenceField
from datetime import datetime, UTC
from flask_login import UserMixin

# relative imports
# ...

# additional imports
import bcrypt


# --------------------------- User Model -----------------------------------


class User(UserMixin, Document):
    email = EmailField(unique=True, required=True)
    username = StringField(unique=True, required=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=datetime.now(UTC))  # utc to keep it universal

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def check_password(self, password):
        return bcrypt.checkpw(self.password.encode(), password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# --------------------------- Post Model -----------------------------------


class Post(Document):
    title = StringField(required=True)
    content = StringField(required=True)
    author = ReferenceField(User, reverse_delete_rule=2)
    created_at = DateTimeField(default=datetime.now(UTC))

    def __repr__(self):
        return f"Post('{self.title}', '{self.content}', '{self.author.username}')"
