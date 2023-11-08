from flask import Blueprint , render_template , session

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/test/<value>')
def set_session(value):
    session['value'] = value
    return f'Passed value is : {value}'


@views.route('/get')
def get_session():
    return f'Active value is : {session.get('value')}'