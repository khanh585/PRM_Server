from flask_server import db
from datetime import datetime
from flask_server.dto.ActorDTO import ActorDTO

class LogDTO(db.Model):
    __tablename__ = 'log'
    user_id = db.Column(db.Integer, db.ForeignKey('actor.actor_id'), primary_key = True)
    date_create = db.Column(db.DateTime,default = datetime.utcnow, primary_key = True)
    action = db.Column(db.String(100), nullable = True)
    user = db.relationship(ActorDTO)

    def serialize(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user.name,
            "date_create": self.date_create,
            "action": self.action,
        }
    

    
