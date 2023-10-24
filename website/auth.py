from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login' , methods=['GET','POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p> logout </p>'

@auth.route('/register' , methods=['GET','POST'])
def register():
    if request == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password_c = request.form.get('password_c')

    return render_template('register.html')