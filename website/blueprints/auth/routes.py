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
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        found_user = User.find_by_username(username)
        # [4]// user_id = str(found_user.get('_id'))
        # [5]// user_id = found_user.get('_id')
        user_id = found_user.get('_id')
        try:
            if found_user and bcrypt.checkpw(password.encode(), found_user['password'].encode()):
                log_user = User(found_user["email"], found_user['username'], found_user["password"])
        # -------------- FAILURE LOG ----------------
                # [2]// login_user(log_user.get_id(), form.remember_me.data)
                # [2]!> UserMixin,get_id() takes 1 positional arguments but two were given.

                # [3]// login_user(log_user, form.remember_me.data)
                # [3]!> No `id` attribute - override `get_id`

                # [4]// login_user(user_id, form.remember_me.data)
                # [4]!> 'str' object has no attribute 'is_active'

                # [5]// login_user(user_id, form.remember_me.data)
                # [5]!> 'ObjectId' object has no attribute 'is_active'
        # -------------------------------------------
                login_user(user_id, form.remember_me.data)
                flash(f'Welcome {found_user["username"]}', 'SUCCESS')
                return redirect(url_for('auth.protected'))

        except Exception as e:
            flash(f'Error during login: {str(e)}', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('login.html', title='Sign In', form=form)


# --------------------------- User Loader -----------------------------------
@login_manager.user_loader
def load_user(username):
    user = User.find_by_username(username)
    if user is not None:
        return user
    else:
        return None


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
def profile():
    user = User.find_by_username(current_user.username).first_or_404()
    return render_template('profile.html', user=user)


# Example protected route
@auth.route('/protected')
@login_required
def protected():
    return f'Hello, {current_user.username}! This is a protected route.'




