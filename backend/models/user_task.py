from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

user_tasks = db.Table('user_tasks',
                      db.Model.metadata,
                      db.Column('users', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
                      db.Column('tasks', db.Integer, db.ForeignKey(add_prefix_for_prod('tasks.id')), primary_key=True)
)
