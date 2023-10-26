from flask import Blueprint, render_template, request, flash
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login' , methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p> logout </p>'

@auth.route('/register' , methods=['GET','POST'])
def register_user():
    data = request.form

    if request == 'POST':
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        new_user = User(username, email, password)
        new_user.save()

        if not username or not email or not password:
            return flash('Missing required fields', 'alert'), 400

        if User.find_by_username(username):
            return flash('Username already exists', 'alert'), 400

        new_user = User(username, email, password)
        new_user.save()
        flash('Registration successful', 'success')


    return render_template('register.html') , 201