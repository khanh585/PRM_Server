from flask_server.dto.LogDTO import LogDTO
from flask_server import db
from sqlalchemy import desc

def dbCreate(new_log):
    
    try:
        db.session.add(new_log)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise e
    return False

def dbRead():
    return LogDTO.query.order_by(desc(LogDTO.date_create)).all()

