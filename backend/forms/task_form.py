from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField
from wtforms.validators import DataRequired, Length, Optional

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    description = StringField('Description', validators=[Length(max=200), Optional()])
    due_date = DateTimeField('Due Date', format='%Y-%m-%d %H:%M:%S', validators=[Optional()])
    status = StringField('Status', validators=[DataRequired(), Length(max=30)])
