from flask_server import db

class CharacterDTO(db.Model):
    __tablename__ = 'character'
    character_id = db.Column(db.Integer, db.ForeignKey('persona.persona_id'),primary_key = True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.actor_id'), primary_key = True)
    tribulation_id = db.Column(db.Integer, db.ForeignKey('tribulation.tribulation_id'), primary_key = True)
