from flask import render_template, request, redirect, Blueprint, jsonify
from flask_server import app

from flask_server.dao import ActorDAO
from flask_server.dto.ActorDTO import ActorDTO

from flask_server.dto.LogDTO import LogDTO
from flask_server.dao import LogDAO
from datetime import datetime



actor = Blueprint('actor', __name__, url_prefix='/admin/actor')



@actor.route('/', methods=['GET'])
def getactor():
    try:
        actors = [actor.serialize() for actor in ActorDAO.dbRead()]
        return jsonify(actors), 200 
    except Exception as e:
        print(e)
        return "Server error", 500

@actor.route('/tribulation/<int:id>', methods=['GET'])
def getActorByTribulationID(id):
    try:
        result = None
        result = [actor.serialize() for actor in ActorDAO.dbGetByTribulationID(id)]
        return jsonify(result), 200 
    except Exception as e:
        print(e)
        return "Server error", 500

@actor.route('/<int:id>', methods=['GET'])
def getactorById(id):
    try:
        actor = ActorDAO.dbGet(id)
        if actor:
            return jsonify(actor.serialize()), 200
        else:
            return jsonify(actor), 200
    except Exception as e:
        print(e)
        return "Server error", 500
    
@actor.route('/', methods=['POST'])
def create():
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        new_actor = ActorDTO(**data)
        result = ActorDAO.dbCreate(new_actor)
        if result > 0:
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "create actor " , date_create = datetime.now())
            LogDAO.dbCreate(log)
            return jsonify(result), 201
        return "Can't create", 403
    except Exception as e:
        print(e)
        return "Server error", 500 

@actor.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        result = ActorDAO.dbDelete(id)
        if result > 0:
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "delete actor id: " + id, date_create = datetime.now())
            LogDAO.dbCreate(log)
            return jsonify(result), 200
            
        return "Can't delete", 403
    except Exception as e:
        print(e)
        if "404 Not Found" in str(e):
            return "404 Not Found", 404
        else:
            return "Server error", 500 

@actor.route('/<int:id>',methods=['PUT'])
def update(id):
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        result = ActorDAO.dbUpdate(id,ActorDTO(**data))
        if result > 0:
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "update actor id: " + id, date_create = datetime.now())
            LogDAO.dbCreate(log)
            return jsonify(result+""), 200
        return "Can't delete", 403
    except Exception as e:
        print(e)
        if "404 Not Found" in str(e):
            return "404 Not Found", 404 
        else:
            return "Server error", 500 
