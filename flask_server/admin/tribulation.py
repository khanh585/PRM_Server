from flask import render_template, request, redirect, Blueprint, jsonify
from datetime import datetime
from flask_server import app
import sys, traceback
from flask_server.dao import TribulationDAO
from flask_server.dao import ToolForTribulationDAO
from flask_server.dao import CharacterDAO
from flask_server.dao import LogDAO

from flask_server.dto.TribulationDTO import TribulationDTO
from flask_server.dto.ToolForTribulationDTO import ToolForTribulationDTO
from flask_server.dto.CharacterDTO import CharacterDTO
from flask_server.dto.LogDTO import LogDTO

tribulation = Blueprint('tribulation', __name__, url_prefix='/admin/tribulation')



@tribulation.route('/', methods=['GET'])
def gettribulation():
    try:
        tribulations = [tribulation.serialize() for tribulation in TribulationDAO.dbRead()]
        return jsonify(tribulations), 200 
    except Exception as e:
        print(e)
        return "Server error", 500

@tribulation.route('/actor/<int:id>', methods=['GET'])
def gettribulationByActorID(id):
    try:
        tribulations = [tribulation.serialize() for tribulation in TribulationDAO.dbGetByActorID(id)]
        return jsonify(tribulations), 200 
    except Exception as e:
        print(e)
        return "Server error", 500


@tribulation.route('/<int:id>', methods=['GET'])
def gettribulationById(id):
    try:
        tribulation = TribulationDAO.dbGet(id)
        if tribulation:
            return jsonify(tribulation.serialize()), 200
        else:
            return jsonify(tribulation), 200
    except Exception as e:
       
        return "Server error", 500
    
@tribulation.route('/', methods=['POST'])
def create():
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        new_tribulation = TribulationDTO(**data)
        result = TribulationDAO.dbCreate(new_tribulation)
        if result > 0:
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "create tribulation", date_create = datetime.now())
            LogDAO.dbCreate(log)
            return jsonify(result), 201
        return "Can't create", 403
    except Exception as e:
        print(e)
        return "Server error", 500 

@tribulation.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        result = TribulationDAO.dbDelete(id)
        if result > 0:
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "delete tribulation" + id, date_create = datetime.now())
            LogDAO.dbCreate(log)
            return jsonify(result), 200
        return "Can't delete", 403
    except Exception as e:
        print(e)
        if "404 Not Found" in str(e):
            return "404 Not Found", 404
        else:
            return "Server error", 500 

@tribulation.route('/<int:id>',methods=['PUT'])
def update(id):
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        result = TribulationDAO.dbUpdate(id,TribulationDTO(**data))

        if result > 0:
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "update tool into tribulation", date_create = datetime.now())
            LogDAO.dbCreate(log)
            return jsonify(result+""), 200
        return "Can't update", 403
    except Exception as e:
        print(e)
        traceback.print_exc(file=sys.stdout)
        if "404 Not Found" in str(e):
            return "404 Not Found", 404 
        else:
            return "Server error", 500 

@tribulation.route('/<int:id>/add-tool',methods=['POST'])
def addTool(id):
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        tft = ToolForTribulationDTO(**data)
        tft.quantity = int(tft.quantity)
        tribulation = TribulationDAO.dbGet(id)
        tft.tribulation_id = id
        tft.time_start = tribulation.time_start
        tft.time_end = tribulation.time_end
        result = ToolForTribulationDAO.dbCreate(tft)
        if result > 0:
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "add tool into tribulation", date_create = datetime.now())
            LogDAO.dbCreate(log)
            return jsonify(result+""), 200
        return "Can't add tool", 403
    except Exception as e:
        print(e)
        if "404 Not Found" in str(e):
            return "404 Not Found", 404 
        else:
            return "Server error", 500 

@tribulation.route('/<int:id>/remove-tool',methods=['PUT'])
def removeTool(id):
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        tool_id = int(data["tool_id"])
        if ToolForTribulationDAO.dbDelete(tool_id,id):
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "remove tool into tribulation", date_create = datetime.now())
            LogDAO.dbCreate(log)
            return "Remove Success", 200
        return "Can't remove tool", 403
    except Exception as e:
        print(e)
        if "404 Not Found" in str(e):
            return "404 Not Found", 404 
        else:
            return "Server error", 500 

@tribulation.route('/<int:id>/update-tool',methods=['PUT'])
def updateTool(id):
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        tft = ToolForTribulationDTO(**data)
        tribulation = TribulationDAO.dbGet(id)
        tft.tribulation_id = id
        tft.time_start = tribulation.time_start
        tft.time_end = tribulation.time_end
        result = ToolForTribulationDAO.dbUpdate(tft)
        if result > 0:
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "add actor into tribulation", date_create = datetime.now())
            LogDAO.dbCreate(log)
            return jsonify(result+""), 200
        return "Can't update tool", 403
    except Exception as e:
        print(e)
        if "404 Not Found" in str(e):
            return "404 Not Found", 404 
        else:
            return "Server error", 500 


@tribulation.route('/<int:id>/add-actor',methods=['POST'])
def addActor(id):
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        character = CharacterDTO(**data)
        character.tribulation_id = id
        result = CharacterDAO.dbCreate(character)
        if result > 0:
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "add actor into tribulation", date_create = datetime.now())
            LogDAO.dbCreate(log)
            return jsonify(result), 200
        return "Can't add tool", 403
    except Exception as e:
        print(e)
        if "404 Not Found" in str(e):
            return "404 Not Found", 404 
        else:
            return "Server error", 500 

@tribulation.route('/<int:id>/remove-actor',methods=['PUT'])
def removeActor(id):
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        character = CharacterDTO(**data)
        character.tribulation_id = id
        if CharacterDAO.dbDelete(character):
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "remove actor into tribulation", date_create = datetime.now())
            LogDAO.dbCreate(log)
            return "Remove Success", 200
        return "Can't remove tool", 403
    except Exception as e:
        print(e)
        if "404 Not Found" in str(e):
            return "404 Not Found", 404 
        else:
            return "Server error", 500 