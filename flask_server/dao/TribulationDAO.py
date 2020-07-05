from flask_server import db
from flask_server.dto.TribulationDTO import TribulationDTO


def dbRead():
    return TribulationDTO.query.order_by(TribulationDTO.name).all()

def dbGet(tribulation_id):
    return TribulationDTO.query.get(tribulation_id)

def dbCreate(new_tribulation):
    try:
        db.session.add(new_tribulation)
        db.session.flush()
        db.session.commit()
        return new_tribulation.tribulation_id
    except Exception as e:
        db.session.rollback()
        raise e
    return -1

def dbUpdate(id,data):
    data = data.serialize()
    try: 
        tribulation_to_update = TribulationDTO.query.get_or_404(id)
        tribulation_to_update.merge(data)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise e
    return False

def dbDelete(id):
    try:
        tribulation_to_delete = TribulationDTO.query.get_or_404(id)
        db.session.delete(tribulation_to_delete)
        db.session.commit()
        return id
    except Exception as e:
        db.session.rollback()
        raise e
    return -1