from flask_server import db
from flask_server.dto.ActorDTO import ActorDTO
from flask_server.dto.CharacterDTO import CharacterDTO


def dbRead():
    return ActorDTO.query.filter(ActorDTO.is_deleted == False).order_by(ActorDTO.name).all()

def dbGetByTribulationID(tribulation_id):
    return db.session.query(ActorDTO).join(CharacterDTO).filter(ActorDTO.is_deleted == False, CharacterDTO.tribulation_id == tribulation_id).all()


def dbGet(actor_id):
    return ActorDTO.query.get(actor_id)

def dbLogin(email, password):
    return ActorDTO.query.filter(ActorDTO.email == email, ActorDTO.password == password).first()

def dbCheckEmailRole(email, role):
    actor = ActorDTO.query.filter(ActorDTO.email == email, ActorDTO.role == role).first()
    if actor:
        return True
    else:
        return False

def dbCreate(new_actor):
    try:
        db.session.add(new_actor)
        db.session.flush()
        db.session.commit()
        return new_actor.actor_id
    except Exception as e:
        db.session.rollback()
        raise e
    return -1

def dbUpdate(id,data):
    data = data.serialize()
    try: 
        actor_to_update = ActorDTO.query.get_or_404(id)
        actor_to_update.merge(data)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise e
    return False

def dbDelete(id):
    try:
        actor_to_delete = ActorDTO.query.get_or_404(id)
        actor_to_delete.is_deleted = True
        db.session.commit()
        return id
    except Exception as e:
        db.session.rollback()
        raise e
    return -1

