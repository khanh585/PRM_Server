from flask_server import db
from flask_server.dto.CharacterDTO import CharacterDTO


def dbCreate(add_actor):
    result = False
    try:
        db.session.add(add_actor)
        db.session.flush()
        db.session.commit()
        result = True
    except Exception as e:
        db.session.rollback()
        raise e
    return result

def dbDelete(delete_actor):
    result = False
    try:
        actor_to_delete = CharacterDTO.query.filter(CharacterDTO.actor_id == delete_actor.actor_id, CharacterDTO.character_id == delete_actor.character_id, CharacterDTO.tribulation_id == delete_actor.tribulation_id).first()
        db.session.delete(actor_to_delete)
        db.session.commit()
        result = True
    except Exception as e:
        db.session.rollback()
        raise e
    return result