from flask_server import db

class PersonaDTO(db.Model):
    __tablename__ = 'persona'
    persona_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(50), nullable = False)
   
    def serialize(self):
        return {
            "persona_id": self.persona_id,
            "name": self.name
        }

    def merge(self,newdata):
        for key,value in newdata.items():
            if value:
                setattr(self,key,value)
