from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateTimeField
from wtforms.validators import DataRequired, Length

class UserWorkspaceForm(FlaskForm):
    role = StringField('Role', validators=[DataRequired(), Length(max=20)])
