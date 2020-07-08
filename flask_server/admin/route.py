from flask import render_template, request, redirect, Blueprint
from flask_server.dao.TodoDAO import *
from flask_server import app
from flask import jsonify
import pyodbc
todo = Blueprint('todo', __name__, url_prefix='/todo')

@todo.route('/', methods=['POST','GET'])
def index():
    for item in pyodbc.drivers():
        print(item)

    return jsonify({"khanh":"ahihi"})



