from flask_server import db
from flask_server.dto.TribulationDTO import TribulationDTO
from flask_server.dto.ActorDTO import ActorDTO
from flask_server.dto.CharacterDTO import CharacterDTO


def dbRead():
    return TribulationDTO.query.filter(TribulationDTO.is_deleted == False).order_by(TribulationDTO.name).all()

def dbGet(tribulation_id):
    return TribulationDTO.query.get(tribulation_id)

def dbGetByActorID(actor_id):
    rs = db.session.query(TribulationDTO).join(CharacterDTO).filter(CharacterDTO.actor_id == actor_id).all()
    for i in rs:
        print(i)
    print(rs)
    return rs
     

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
    try: 
        tribulation_to_update = TribulationDTO.query.get_or_404(id)
        tribulation_to_update.merge(data.__dict__)
        db.session.commit()
        print(tribulation_to_update.time_end)
        return True
    except Exception as e:
        db.session.rollback()
        raise e
    return False

def dbDelete(id):
    try:
        tribulation_to_delete = TribulationDTO.query.get_or_404(id)
        tribulation_to_delete.is_deleted = True
        db.session.commit()
        return id
    except Exception as e:
        db.session.rollback()
        raise e
    return -1




