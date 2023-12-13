# from .db import db, environment, SCHEMA, add_prefix_for_prod
# from datetime import datetime

# class Role(db.Model):
#     __tablename__ = 'roles'

#     if environment == 'production':
#         __table_args__ = {'schema': SCHEMA}

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     description = db.Column(db.String(200))

#     def to_dict(self):
#         return {
#             'id':self.id,
#             'name':self.name,
#             'description': self.description
#         }
