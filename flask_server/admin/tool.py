from flask import render_template, request, redirect, Blueprint, jsonify
from flask_server import app

from flask_server.dao import ToolDAO
from flask_server.dto.ToolDTO import ToolDTO
from flask_server.dto.LogDTO import LogDTO
from flask_server.dao import LogDAO
from flask_server.util.authentication import verify
from datetime import datetime

tool = Blueprint('tool', __name__, url_prefix='/admin/tool')

ROLE_ADMIN = 'admin'
ROLE_ACTOR = 'actor'


@tool.route('/', methods=['GET'])
def getTool():
    try:
       
        result = None
        result = [tool.serialize() for tool in ToolDAO.dbRead()]
        return jsonify(result), 200 
    except Exception as e:
        print(e)
        return "Server error", 500

    

@tool.route('/<int:id>', methods=['GET'])
def getToolById(id):
    try:
        tool = ToolDAO.dbGet(id)
        if tool:
            return jsonify(tool.serialize()), 200
        else:
            return jsonify(tool), 200
    except Exception as e:
        print(e)
        return "Server error", 500
    
@tool.route('/', methods=['POST'])
def index():
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        new_tool = ToolDTO(**data)
        result = ToolDAO.dbCreate(new_tool)
        if result > 0:
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "add actor into tribulation", date_create = datetime.now())
            LogDAO.dbCreate(log)
            return jsonify(result), 201
        return "Can't create", 403
    except Exception as e:
        print(e)
        return "Server error", 500 

@tool.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        result = ToolDAO.dbDelete(id)
        if result > 0:
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "add actor into tribulation", date_create = datetime.now())
            LogDAO.dbCreate(log)
            return jsonify(result), 200
        return "Can't delete", 403
    except Exception as e:
        if "404 Not Found" in str(e):
            return "404 Not Found", 404
        else:
            return "Server error", 500 

@tool.route('/<int:id>',methods=['PUT'])
def update(id):
    if not request.is_json:
        return "Bad Request", 403
    try:
       
        data = request.get_json()
        result = ToolDAO.dbUpdate(id,ToolDTO(**data))
        if result > 0:
            user_id = request.headers['UserID']
            log = LogDTO(user_id = user_id, action = "add actor into tribulation", date_create = datetime.now())
            LogDAO.dbCreate(log)
            return jsonify(result), 200
        return "Can't delete", 403
    except Exception as e:
        if "404 Not Found" in str(e):
            return "404 Not Found", 404 
        else:
            return "Server error", 500 
