from pymongo import MongoClient
from datetime import datetime, UTC

import bcrypt

client = MongoClient('localhost', 27017)
db = client['profiles']
collection = db['Users']
Posts = db['Posts']


class User:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        # datetime.now(tz=None) // gives local time
        self.created_at = datetime.now(UTC)

    def to_dict(self):
        return {
            'email': self.email,
            'username': self.username,
            'password': self.password.decode(),
            'created_at': self.created_at
        }

    def save(self):
        user_data = self.to_dict()
        result = collection.insert_one(user_data)
        return result.inserted_id

    @classmethod
    def from_dict(cls, data):
        user = cls(data['email'], data['username'], data['password'])
        if 'created_at' in data:
            user.created_at = data['created_at']
        return user

    @classmethod
    def find_by_username(cls, username):
        user_data = collection.find_one({'username': username})
        if user_data:
            return user_data
        return None

    @classmethod
    def find_by_email(cls, email):
        email_data = collection.find_one({'email': email})
        if email_data:
            return email_data
        return None

    def check_password(self, password):
        try:
            # Note: The stored password is already in bytes, so no need to encode it
            return bcrypt.checkpw(password, self.password)

        except Exception as e:
            # Handle exceptions (e.g., invalid hashing format, incorrect input)
            print(f"Error checking password: {e}")
            return False


class Post:
    def __init__(self, id, title, content, date_posted):
        self.id = id
        self.title = title
        self.content = content
        self.date_posted = date_posted

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
