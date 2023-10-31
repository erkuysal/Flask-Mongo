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

        # Login Confirmed
        if pass:
            if pass:
                flash('Welcome back!', 'SUCCESS')
                return redirect(url_for('success.html'))
        # Login Denied
        else:
            flash('I have never met this man in my life !', 'DENIED')
            return redirect(url_for('denied.html'))


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