from flask import Blueprint, render_template, request, redirect, url_for, flash
from .get_database import get_database
from .models import User

# Sessions

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
                    # sess['user_id'] = user['_id']  # Store the user's ID in the session
                    flash(f'Welcome back {user.get('username')}', 'SUCCESS')
                    print('correct password')
                    return redirect(url_for('auth.profile'))  # Redirect to the user's profile page

        except:
            if username != user.get('username'):
                flash('I never met this man in my life', 'NULL')
                print('not a registered user!')

    return render_template('login.html')


@auth.route('/logout')
def logout():
    # sess.pop('user_id', None)  # Clear the user's session
    flash('You have been logged out', 'SUCCESS')
    # TODO: return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        User.save(User(email, username, password))
        flash('Welcome to the Club', 'SUCCESS')

    profiles = Users.find()
    return render_template('register.html', todos=profiles)


# @auth.route('/profile')
# def profile():
#     if 'user_id' in session:
#         # User is logged in, fetch user data from the database
#         user_id = session['user_id']
#         user = Users.find_one({'_id': user_id})
#
#         # Render the user's profile page with their data
#         return render_template('profile.html', user=user)
#     else:
#         # User is not logged in, redirect to the login page
#         return redirect(url_for('auth.login'))
