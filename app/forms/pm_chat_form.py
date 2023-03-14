from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, URL


class PmChatForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    user1_id = IntegerField('ID', validators=[DataRequired()])
    user2_id = IntegerField('ID', validators=[DataRequired()])
    submit = SubmitField('Submit')
