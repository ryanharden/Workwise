from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Notification(db.Model):
    __tablename__ = "notifications"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    link = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    user = db.relationship("User", back_populates="notifications")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'message': self.message,
            'status': self.status,
            'link': self.link,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
