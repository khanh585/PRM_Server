from flask_server import db
from flask_server.dto.CharacterDTO import CharacterDTO

class ActorDTO(db.Model):
    __tablename__ = 'actor'
    actor_id = db.Column(db.Integer, primary_key = True, autoincrement=True) 
    name = db.Column(db.String(50), nullable = False)
    image = db.Column(db.String(500), nullable = True)
    description = db.Column(db.String(500), nullable = True)
    phone = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(20) ,nullable = False, default = '123')
    role = db.Column(db.String(5), nullable = False, default = 'actor')
    is_deleted = db.Column(db.Boolean(), default = False)
    
    def serialize(self):
        return {
            "actor_id": self.actor_id,
            "name": self.name,
            "image": self.image,
            "description": self.description,
            "phone": self.phone,
            "email": self.email,
            "role": self.role,
        }
    
    def merge(self,newdata):
        for key,value in newdata.items():
            if value:
                setattr(self,key,value)