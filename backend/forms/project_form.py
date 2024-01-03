from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError, Length

class ProjectForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2,max=50)])
    description = StringField('Description', validators=[Length(max=200)])
