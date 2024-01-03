from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError
from backend.models import Workspace

class WorkspaceForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = TextAreaField("Description")
    visibility = StringField("Visibility", validators=[DataRequired()])
