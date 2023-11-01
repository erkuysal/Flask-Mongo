from flask import Blueprint, render_template, request, redirect, url_for, flash
from .get_database import get_database

dbname = get_database()
Users = dbname["users"]

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
                if password != user.get('password'):
                    print('wrong password')
                else:
                    print('correct password')
        except:
            print('not a registered user!')





        # user = Users.find_one({'username' : username})
        #
        # check_name = user.get('username')
        # check_password = user.get('password')
        #
        # if username == check_name:
        #     print('CORRECT NAME')
        #     if password != check_password:
        #         print('ACCESS DENIED!')
        #     else:
        #         print('ACCESS GRANTED!')
        # else:
        #     print('USER NOT FOUND.')

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
        Users.insert_one({'email': email,
                          'username': username,
                          'password': password
                          })
        flash('Welcome to the Club', 'SUCCESS')

    profiles = Users.find()
    return render_template('register.html', todos=profiles)