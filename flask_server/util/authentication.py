from flask_server.dto.ActorDTO import ActorDTO
from flask_server.dao import ActorDAO
from flask import request, redirect, Blueprint, jsonify
from flask_server import app
import jwt
import datetime
import sys, traceback


authentication = Blueprint('authentication', __name__, url_prefix='/login')
secret_key = app.config["SECRET_KEY"]

@authentication.route('/', methods=['POST'])
def login():
    if not request.is_json:
        return "Bad Request", 403
    try:
        data = request.get_json()
        email =  data["email"]
        password = data["password"]
        user = ActorDAO.dbLogin(email, password)
        if not user:
            return "Don't have user", 401
        
        payload = {
            "email":email,
            "role": user.role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        }
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        return jsonify({"Authorization":token.decode("UTF-8"), "UserID":user.actor_id}), 200
    except Exception as e:
        traceback.print_exc(file=sys.stdout)
    return "Server error internal", 500

def verify(role):
    try:
        token = request.headers['Authorization']
        decode =  jwt.decode(token, secret_key, algorithms=['HS256'])
        # check exp
        exp = decode["exp"]
        now = datetime.datetime.now()
        exp = datetime.datetime.fromtimestamp(exp)
        check_exp = now <= exp

        # check role
        check_role = decode["role"] in role


        return check_exp and check_role  # and check_email_role
    except Exception as e:
        print(e)
        return False
