from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from backend.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')

def password_length(form, field):
    password = field.data
    if len(password) < 7:
        raise ValidationError("Password must be at least 7 characters long")

def name_length(form, field):
    first_name = field.data
    last_name = field.data
    if len(first_name) < 2:
        raise ValidationError("First Name must be more 2 characters")
    if len(last_name) < 2:
        raise ValidationError("Last Name must be more 2 characters")
    if len(first_name) > 25:
        raise ValidationError("First Name must be less than 25 characters")
    if len(last_name) > 25:
        raise ValidationError("Last Name must be less than 25 characters")


class SignUpForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), username_exists])
    email = StringField('email', validators=[DataRequired(), user_exists])
    password = StringField('password', validators=[DataRequired(), password_length])
    first_name = StringField('first_name', validators=[DataRequired(), name_length])
    last_name = StringField('first_name', validators=[DataRequired(), name_length])
    image_url = StringField('image_url')
