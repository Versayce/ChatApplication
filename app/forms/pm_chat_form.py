from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, URL


class PmChatForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    user1_id = IntegerField('ID1')
    user2_id = IntegerField('ID2')
    submit = SubmitField('Submit')
