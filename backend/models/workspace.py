from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Workspace(db.Model):
    __tablename__ = "workspaces"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    visibility = db.Column(db.String(20), nullable=False)
    workspace_image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'owner_id': self.owner_id,
            'visibility': self.visibility,
            'workspace_image_url': self.workspace_image_url,
            'updated_at': self.updated_at
        }
