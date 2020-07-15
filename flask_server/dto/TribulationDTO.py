from flask_server import db
from datetime import datetime
from flask_server.dto.ActorDTO import ActorDTO
from flask_server.dto.ToolDTO import ToolDTO
from flask_server.dto.ToolForTribulationDTO import ToolForTribulationDTO

class TribulationDTO(db.Model):
    __tablename__ = 'tribulation'
    tribulation_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(500), nullable = True)
    address = db.Column(db.String(200), nullable = True)
    time_start = db.Column(db.DateTime,default= datetime.utcnow)
    time_end = db.Column(db.DateTime,default= datetime.utcnow)
    times = db.Column(db.Integer, default = 1)
    url_file = db.Column(db.String(200), nullable = True)
    actor = db.relationship(ActorDTO, secondary='character', backref="tribulation")
    tool = db.relationship(ToolDTO, secondary='tool_for_tribulation', backref="tribulation")
    is_deleted = db.Column(db.Boolean(), default = 0)


    def serialize(self):
        actor = [a.serialize() for a in self.actor]
        tool = [t.serialize() for t in self.tool]
        time_start = self.time_start.strftime("%Y-%m-%d")
        time_end = self.time_end.strftime("%Y-%m-%d")
        return {
            "tribulation_id": self.tribulation_id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "time_start": time_start,
            "time_end": time_end,
            "times": self.times,
            "url_file": self.url_file,
            "actor": actor,
            "tool": tool
        }
    
    def merge(self,newdata):
        for key,value in newdata.items():
            if value:
                setattr(self,key,value)