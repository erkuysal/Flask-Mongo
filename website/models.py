# Package imports
from mongoengine import signals
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


class Post(dbase.Document):
    title = dbase.StringField(required=True)
    content = dbase.StringField(required=True)
    # author = dbase.ReferenceField(User, reverse_delete_rule=dbase.CASCADE)
    # !> TypeError: WtfFieldMixin.__init__() takes 1 positional argument but 2 were given

# def pre_delete_post(sender, document, **kwargs):
#     # Handle cascading delete when a Post is deleted
#     User.objects(id=document.author.id).update(pull__posts=document.id)
#
#
# # Connect the pre_delete_post function to the pre_delete signal of the Post model
# signals.pre_delete.connect(pre_delete_post, sender=Post)
