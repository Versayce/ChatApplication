from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, URL


class ChannelForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    user1_id = IntegerField('User1_id', validators=[DataRequired()])
    user2_id = IntegerField('User2_id', validators=[DataRequired()])
    submit = SubmitField('Submit')
