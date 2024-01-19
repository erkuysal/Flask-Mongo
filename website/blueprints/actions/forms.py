from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms.fields import *

from flask_wtf.file import FileField


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=1, max=280)])
    submit = SubmitField('Post')


class UploadForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Upload')
    delete = SubmitField('Delete')
    