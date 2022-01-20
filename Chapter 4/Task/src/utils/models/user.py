from email.policy import default
from utils.db import db
import uuid

class User(db.Model):
    task_id = db.Column(db.String(32), primary_key= True, default=str(uuid.uuid4()))
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    #done = db.Column(db.Boolean, nullable=False, default= False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    changed_at = db.Column(db.DateTime, nullable=False, default=db.func.now())

    def to_json(self):
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            #'done': self.done,
            'created_at': str(self.created_at), 
            'changed_at': str(self.changed_at) 
        }