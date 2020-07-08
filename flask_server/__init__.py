from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib

# Connect to DB
params = urllib.parse.quote_plus("DRIVER={FreeTDS};"
                                 "SERVER=58.186.23.68;"
                                 "DATABASE=Khanh_PRM;"
                                 "UID=htd0910;"
                                 "PWD=123456"
                                 )


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect={}".format(params)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'khanh585'
db = SQLAlchemy(app)



from flask_server.admin.route import todo
from flask_server.admin.tool import tool
from flask_server.admin.actor import actor
from flask_server.admin.tribulation import tribulation
from flask_server.admin.persona import persona
from flask_server.util.authentication import authentication
app.register_blueprint(todo)
app.register_blueprint(tool)
app.register_blueprint(actor)
app.register_blueprint(tribulation)
app.register_blueprint(persona)
app.register_blueprint(authentication)
