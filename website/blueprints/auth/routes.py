from flask import render_template, request, redirect, url_for, flash, session
import bcrypt

from ...db import get_database
from ...models import User, db

from . import auth
from .forms import *

dbname = get_database()
Users = dbname["Users"]


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = SignInForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data

        # TODO: Validation
        existing_user = User.find_by_username(username)
        try:
            if username == existing_user['username']:
                print('correct username')

                if bcrypt.checkpw(password.encode(), existing_user.get('password').encode()) is False:
                    flash('Wrong Password', 'DENIED')
                    print('wrong password')
                else:
                    session['user'] = existing_user.get('username')
                    flash(f'Welcome back {existing_user.get('username')}', 'SUCCESS')
                    print('correct password')
                    return redirect(url_for('auth.profile'))  # Redirect to the user's profile page

        except Exception as e:
            if existing_user is None:
                flash('I never met this man in my life', 'NULL')
                print(f'not a registered user! {e}')
                return redirect(url_for('auth.register'))

    return render_template('login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('Form Validated!')
        User.save(User(form.email.data, form.username.data, form.password.data))
        return redirect(url_for('auth.login'))

    profiles = Users.find()
    return render_template('register.html', todos=profiles,
                           form=form)


@auth.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out', 'SUCCESS')
    return redirect(url_for('auth.login'))


@auth.route('/profile')
def profile():
    if 'user' in session:
        user = session['user']
        return render_template('profile.html')
    else:
        return redirect(url_for('auth.login'))

