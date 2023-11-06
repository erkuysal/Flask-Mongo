from flask import Blueprint, render_template, request, redirect, url_for, flash
from .get_database import get_database
from .models import User

# Sessions
from flask import session
from flask_session import Session

dbname = get_database()
Users = dbname["Users"]

auth = Blueprint('auth', __name__)

@auth.route('/login' , methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # TODO: Validation

        try:
            user = Users.find_one({'username': username})

            if username == user.get('username'):
                print('correct username')
                if password == user.get('password'):
                    flash('Wrong Password', 'DENIED')
                    print('wrong password')
                else:
                    flash(f'Welcome back {user.get('username')}','SUCCESS')
                    print('correct password')
        except:
            flash('I never met this man in my life' , 'NULL')
            print('not a registered user!')

    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p> logout </p>'

@auth.route('/register' , methods=['GET','POST'])
def register_user():
    if request.method =='POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        User.save(User(username, password, password))
        flash('Welcome to the Club', 'SUCCESS')

    profiles = Users.find()
    return render_template('register.html', todos=profiles)