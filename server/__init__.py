from flask import Flask, Blueprint, request
from flask_mongoengine import MongoEngine
from server.routes import create_routes
from server import utils
from server import models

def create_app():
    app = Flask(__name__)
    app.register_blueprint(create_routes(Blueprint, request, utils, models))

    app.config['MONGODB_SETTINGS'] = {
        'db': 'sorverte',
        'host': 'mongodb://localhost:27017',
        'connect': False
    }
    #app.config['MONGO_CONNECT'] = False
    db = MongoEngine()
    db.init_app(app)

    return app
