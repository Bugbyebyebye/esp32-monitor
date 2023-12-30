from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:maojiukeai1412@222.186.50.126:20134/df_esp32'
db = SQLAlchemy(app)

from routes import video
from routes import mqtt
from routes import data
from routes import user
from routes import warn
