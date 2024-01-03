from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class NotificationForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2,max=50)])
    message = StringField('Message', validators=[DataRequired(), Length(min=2)])
    status = StringField('Status', validators=[DataRequired()])
    link = StringField('Link')
