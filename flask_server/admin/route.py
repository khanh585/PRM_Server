from flask import render_template, request, redirect, Blueprint
from flask_server.dao.TodoDAO import *
from flask_server import app
from flask import jsonify
todo = Blueprint('todo', __name__, url_prefix='/todo')

@todo.route('/', methods=['POST','GET'])
def index():
    return jsonify({"khanh":"ahihi"})



