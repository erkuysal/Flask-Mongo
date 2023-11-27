from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms.fields import *

from flask_bootstrap import SwitchField


class SignUpForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(),
                                    Length(1, 50)])
    username = StringField('Username',
                           validators=[DataRequired(),
                                       Length(1, 20)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(8, 150),
                                         EqualTo('password_c', message='Passwords must match.')])
    password_c = PasswordField('Confirm password',
                               validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')
