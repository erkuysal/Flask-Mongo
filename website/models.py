from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
import datetime

client = MongoClient ('localhost', 27017)
db = client['profiles']
collection = db['Users']


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.created_at = datetime.datetime.utcnow()

    @classmethod
    def from_dict(cls, data):
        user = cls(data['username'], data['email'], data['password'])
        if 'created_at' in data:
            user.created_at = data['created_at']
        return user

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'created_at': self.created_at
        }

    def save(self):
        user_data = self.to_dict()
        result = collection.insert_one(user_data)
        return result.inserted_id

    @classmethod
    def find_by_username(cls, username):
        user_data = collection.find_one({'username': username})
        if user_data:
            return cls.from_dict(user_data)
        return None

    def check_password(self, password):
        return check_password_hash(self.password, password)
