# Package imports
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime, UTC
import bcrypt

# Model imports
from ...models import User, db
from ... import login_manager

# Inner imports
from . import auth
from .forms import *

# Collections
dbname = db
Users = dbname["Users"]


@auth.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now(UTC)


#  ------------------------------ Sign Up Section --------------------------------------


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        existing_username = User.find_by_username(username)
        existing_email = User.find_by_email(email)

        if existing_username:    # Check if the username is already taken
            flash('Existing Username!')
            return redirect(url_for('auth.register'))

        elif existing_email:    # Check if the email is already taken
            flash('Existing Email!')
            return redirect(url_for('auth.register'))

        else:
            flash('Form Validated!')
            new_user = User(form.email.data, form.username.data, form.password.data)
            User.save(new_user)
            return redirect(url_for('auth.login'))

    profiles = Users.find()
    return render_template('register.html', todos=profiles,
                           form=form)


@auth.route('/check_username', methods=['POST'])
def check_username():
    form = SignUpForm()
    username = form.username.data

    # Check if the username is already taken
    existing_username = User.find_by_username(username)

    if existing_username:
        message = 'Username is already taken. Please choose a different one.'
        available = False
    else:
        message = 'Username is available!'
        available = True

    return jsonify({'message': message, 'available': available})


#  ------------------------------ Sign In Section --------------------------------------


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

                if bcrypt.checkpw(password.encode(), existing_user.get('password').encode()) is False:
                    flash('Wrong Password', 'DENIED')
                else:
                    login_user(existing_user, form.remember_me.data)
                    # flash(f'Welcome back {existing_user.get('username')}', 'SUCCESS')
                    return redirect(url_for('auth.profile'))  # Redirect to the user's profile page

        except Exception as e:
            if existing_user is None:
                flash('I never met this man in my life', 'NULL')
                print(f'not a registered user! {e}')
                return redirect(url_for('auth.register'))

    return render_template('login.html', form=form)


#  ------------------------------ Log Out Section --------------------------------------


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'SUCCESS')
    return redirect(url_for('auth.login'))


#  ------------------------------ Profile Section --------------------------------------


@auth.route('/profile')
@login_required
def profile(username):
    user = User.find_by_username(username).first_or_404()
    return render_template('profile.html', user=user)




