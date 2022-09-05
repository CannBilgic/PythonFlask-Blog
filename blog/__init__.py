from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db=SQLAlchemy()
class Config(object):
    SECRET_KEY="test"
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:12345@localhost:5432/Blog'

def createApp():
    app= Flask(__name__)
    # app.config['CORS_ALLOW_HEADERS']='*'
    # app.config['CORS_ORIGINS']='*'
    # app.config['CORS_SUPPORTS_CREDENTIALS']=False
    # app.config['CORS_METHOD']=["GET","HEAD","POST","OPTIONS","PUT","PATCH","DELETE"]
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SECRET_KEY']=Config.SECRET_KEY
    db.init_app(app)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    return app