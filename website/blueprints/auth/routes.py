# Package imports
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime, UTC
import bcrypt
from mongoengine.queryset import Q

# Model imports
from ...models import User, Post  # , pre_delete_post
from ... import login_manager

# Inner imports
from . import auth
from .forms import *

# Collections


# @auth.before_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.last_seen = datetime.now(UTC)


#  ------------------------------ Sign Up Section --------------------------------------
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        # existing_user = User.objects(Q(email=email) | Q(username=username)).first()
        existing_username = User.objects(Q(email=email)).first()
        existing_email = User.objects(Q(username=username)).first()

        if existing_username:    # Check if the username is already taken
            flash('Existing Username!')
            return redirect(url_for('auth.register'))

        elif existing_email:    # Check if the email is already taken
            flash('Existing Email!')
            return redirect(url_for('auth.register'))

        else:
            flash('Form Validated!')
            new_user = User(email=form.email.data, username=form.username.data)
            new_user.set_password(form.password.data)
            User.save(new_user)
            return redirect(url_for('auth.login'))

    # profiles = Users.find()
    return render_template('auth/register.html',  # todos=profiles,
                           form=form)


@auth.route('/check_username', methods=['POST'])
def check_username():
    form = SignUpForm()
    username = form.username.data

    # Check if the username is already taken
    existing_username = User.objects(Q(username=username)).first()

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

        found_user = User.objects(Q(username=username)).first()

        try:
            if found_user and bcrypt.checkpw(password.encode(), found_user['password'].encode()):
                login_user(found_user)
                flash(f'Welcome {found_user["username"]}', 'SUCCESS')
                return redirect(url_for('auth.profile'))

            elif bcrypt.checkpw(password.encode(), found_user['password'].encode()) is False:
                flash('Wrong Password', 'DENIED')
                return redirect(url_for('auth.login'))

            else:
                flash('User does not exist!', 'NULL')
                return redirect(url_for('auth.login'))

        except Exception as e:
            flash(f'Error during login: {str(e)}', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html', title='Sign In', form=form)


# --------------------------- User Loader -----------------------------------
@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()


#  ------------------------------ Log Out Section --------------------------------------
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'SUCCESS')
    return redirect(url_for('main.home'))


#  ------------------------------ Profile Section --------------------------------------
@auth.route('/profile')
@login_required
def profile():
    user = current_user  # Assuming you are using Flask-Login
    user_posts = Post.objects(author=user.username)
    all_posts = Post.objects()

    return render_template('profile.html', user_posts=user_posts, feed_posts=all_posts, title='Profile')


#  ------------------------------ Posts Section --------------------------------------
@auth.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, content=form.content.data, author=current_user)
        new_post.save()
        flash('Post created successfully!', 'SUCCESS')
        return redirect(url_for('auth.profile'))
    return render_template('main/feed.html', form=form)


# @auth.route('/delete_post/<post_id>', methods=['GET', 'POST'])
# @login_required
# def delete_post(post_id):
#     post = Post.objects(id=post_id).first()
#
#     # Ensure the user deleting the post is the author
#     if post and post.author == current_user:
#         post.delete()
#         return redirect(url_for('feed'))
#
#     # Handle cases where the post does not exist or the user is not the author
#     flash('Unable to delete the post.', 'danger')
#     return redirect(url_for('feed'))
