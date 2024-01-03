from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length

class CommentForm(FlaskForm):
    body = StringField('Body', validators=[DataRequired(), Length(min=0,max=255, message='Comments must be between 2 and 255 characters'), Length(min=2, message='Comments must be between 2 and 255 characters')])
