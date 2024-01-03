from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Comment(db.Model):
    __tablename__ = 'comments'

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    comment_id = db.Column(db.Integer,db.ForeignKey('comments.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    body = db.Column(db.Text, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow())
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def to_dict(self):
        return {
            'id': self.id,
            'task_id': self.task_id,
            'comment_id': self.comment_id,
            'author_id': self.author_id,
            'body': self.body,
            'created_at': self.createdAt,
            'updated_at': self.updatedAt
        }