from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms.fields import *


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=1, max=280)])
    submit = SubmitField('Post')
