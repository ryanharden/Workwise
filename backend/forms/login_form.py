from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from backend.models import User


def user_exists(form, field):
    # Checking if user exists
    user_input = field.data
    user = User.query.filter((User.email == user_input) | (User.username == user_input)).first()
    if not user:
        raise ValidationError('Username or Email provided not found.')


def password_matches(form, field):
    # Checking if password matches
    password = field.data
    user_input = form.data['user_input']
    user = User.query.filter((User.email == user_input) | (User.username == user_input)).first()
    if not user:
        raise ValidationError('No such user exists.')
    if not user.check_password(password):
        raise ValidationError('Password was incorrect.')


class LoginForm(FlaskForm):
    user_input = StringField('user_input', validators=[DataRequired(), user_exists])
    password = StringField('password', validators=[DataRequired(), password_matches])
