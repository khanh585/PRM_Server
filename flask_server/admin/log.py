from flask import render_template, request, redirect, Blueprint, jsonify
from flask_server import app

from flask_server.dto.LogDTO import LogDTO
from flask_server.dao import LogDAO
from datetime import datetime

log = Blueprint('log', __name__, url_prefix='/log')


@log.route('/', methods=['GET'])
def getTool():
    try:
        result = None
        result = [log.serialize() for log in LogDAO.dbRead()]
        return jsonify(result), 200 
    except Exception as e:
        print(e)
        return "Server error", 500
