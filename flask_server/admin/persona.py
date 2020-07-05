from flask import render_template, request, redirect, Blueprint, jsonify
from flask_server import app

from flask_server.dao import PersonaDAO
from flask_server.dto.PersonaDTO import PersonaDTO


persona = Blueprint('persona', __name__, url_prefix='/admin/persona')



@persona.route('/', methods=['GET'])
def getpersona():
    try:
        personas = [persona.serialize() for persona in PersonaDAO.dbRead()]
        return jsonify(personas), 200 
    except Exception as e:
        print(e)
        return "Server error", 500

@persona.route('/<int:id>', methods=['GET'])
def getpersonaById(id):
    try:
        persona = PersonaDAO.dbGet(id)
        if persona:
            return jsonify(persona.serialize()), 200
        else:
            return jsonify(persona), 200
    except Exception as e:
        print(e)
        return "Server error", 500
    
@persona.route('/', methods=['POST'])
def create():
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        new_persona = PersonaDTO(**data)
        result = PersonaDAO.dbCreate(new_persona)
        if result > 0:
            return jsonify(result), 201
        return "Can't create", 403
    except Exception as e:
        print(e)
        return "Server error", 500 

@persona.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        result = PersonaDAO.dbDelete(id)
        if result > 0:
            return jsonify(result), 200
        return "Can't delete", 403
    except Exception as e:
        if "404 Not Found" in str(e):
            return "404 Not Found", 404
        else:
            return "Server error", 500 

@persona.route('/<int:id>',methods=['PUT'])
def update(id):
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        result = PersonaDAO.dbUpdate(id,PersonaDTO(**data))
        if result > 0:
            return jsonify(result), 200
        return "Can't delete", 403
    except Exception as e:
        if "404 Not Found" in str(e):
            return "404 Not Found", 404 
        else:
            return "Server error", 500 
