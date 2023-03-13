from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, BooleanField, IntegerField
from wtforms.validators import DataRequired, URL


class PmMessageForm(FlaskForm):
    body = StringField('Message', validators=[DataRequired()])
    # image_url = StringField('Image', validators=[URL()])
    chat_id = IntegerField('Chat Id')
    author_id = IntegerField('Author Id')
    submit = SubmitField('Submit')
