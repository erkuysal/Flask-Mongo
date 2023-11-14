from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms.fields import *

from flask_bootstrap import SwitchField


class HelloForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField('Remember me')
    submit = SubmitField()


class ButtonForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    confirm = SwitchField('Confirmation')
    submit = SubmitField()
    delete = SubmitField()
    cancel = SubmitField()


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
    submit = SubmitField()
