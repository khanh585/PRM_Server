from flask_server import db

class ToolDTO(db.Model):
    __tablename__ = 'tool'
    tool_id = db.Column("tool_id",db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(50), nullable = False)
    image = db.Column(db.String(500), nullable = True)
    description = db.Column(db.String(500), nullable = True)
    quantity = db.Column(db.Integer, default = 0)
    status = db.Column(db.String(20), nullable = True)
    is_deleted = db.Column(db.Boolean(), default = 0)

    def serialize(self):
        return {
            "tool_id": self.tool_id,
            "name": self.name,
            "image": self.image,
            "description": self.description,
            "quantity": self.quantity,
            "status": self.status,
            "is_deleted": self.is_deleted,
        }
    
    def merge(self,newdata):
        for key,value in newdata.items():
            if value:
                setattr(self,key,value)
