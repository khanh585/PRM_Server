from flask_server import db
from flask_server.dto.PersonaDTO import PersonaDTO


def dbRead():
    return PersonaDTO.query.order_by(PersonaDTO.name).all()

def dbGet(persona_id):
    return PersonaDTO.query.get(persona_id)

def dbCreate(new_persona):
    try:
        db.session.add(new_persona)
        db.session.flush()
        db.session.commit()
        return new_persona.persona_id
    except Exception as e:
        db.session.rollback()
        raise e
    return -1

def dbUpdate(id,data):
    data = data.serialize()
    try: 
        persona_to_update = PersonaDTO.query.get_or_404(id)
        persona_to_update.merge(data)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise e
    return False

def dbDelete(id):
    try:
        persona_to_delete = PersonaDTO.query.get_or_404(id)
        db.session.delete(persona_to_delete)
        db.session.commit()
        return id
    except Exception as e:
        db.session.rollback()
        raise e
    return -1