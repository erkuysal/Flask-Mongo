from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .get_database import get_database
from .models import User

dbname = get_database()
Users = dbname["Users"]

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # TODO: Validation
        user = Users.find_one({'username': username})

        try:
            if username == user.get('username'):
                print('correct username')

                if password != user.get('password'):
                    flash('Wrong Password', 'DENIED')
                    print('wrong password')
                else:
                    session['user'] = user.get('username')
                    flash(f'Welcome back {user.get('username')}', 'SUCCESS')
                    print('correct password')
                    return redirect(url_for('auth.profile'))  # Redirect to the user's profile page

        except:
            if user is None:
                flash('I never met this man in my life', 'NULL')
                print('not a registered user!')
                return redirect(url_for('auth.register'))

    return render_template('login.html')


@auth.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out', 'SUCCESS')
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        User.save(User(email, username, password))
        flash('Welcome to the Club', 'SUCCESS')
        return redirect(url_for('auth.login'))  # Redirect to the login page after registration

    profiles = Users.find()
    return render_template('register.html', todos=profiles)


@auth.route('/profile')
def profile():
    if 'user' in session:
        user = session['user']
        return render_template('profile.html')
    else:
        return redirect(url_for('auth.login'))

