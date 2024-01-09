from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class UserWorkspace(db.Model):
    __tablename__ = "user_workspaces"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    workspace_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("workspaces.id")), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    joined = db.Column(db.DateTime, default= datetime.utcnow())

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'workspace_id': self.workspace_id,
            'role':self.role,
            'joined':self.joined
        }
