from flask_server import db
from datetime import datetime

class ToolForTribulationDTO(db.Model):
    __tablename__ = 'tool_for_tribulation'
    tribulation_id = db.Column(db.Integer, db.ForeignKey('tribulation.tribulation_id'), primary_key = True)
    tool_id = db.Column(db.Integer, db.ForeignKey('tool.tool_id'), primary_key = True)
    time_start = db.Column(db.DateTime,default = datetime.utcnow)
    time_end = db.Column(db.DateTime,default = datetime.utcnow)
    quantity = db.Column(db.Integer, default = 0)


    def serialize(self):
        return {
            "tribulation_id": self.tribulation_id,
            "tool_id": self.tool_id,
            "time_start": self.time_start,
            "time_end": self.time_end,
            "quantity": self.quantity
        }
    
    def merge(self,newdata):
        for key,value in newdata.items():
            if value:
                setattr(self,key,value)
    
