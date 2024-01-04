from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    image_url = db.Column(db.String(255))
    hashed_password = db.Column(db.String(255), nullable=False)

    workspaces = db.relationship("Workspace", secondary="user_workspaces", back_populates="users")
    tasks = db.relationship("Task", secondary="user_tasks", back_populates="users")
    projects = db.relationship("Project", back_populates="owner")
    notifications = db.relationship("Notification", back_populates="user")
    comments = db.relationship("Comment", back_populates="author")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'image_url': self.image_url,
            'username': self.username,
            'email': self.email
        }
