# -*- coding: utf-8 -*-

from flask import Flask
from config import config

import json
from bson import ObjectId

from .api import configure_api
from .db import mongo


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config["MONGO_URI"] = app.config['MONGODB_HOST']
    
    mongo.init_app(app)
    configure_api(app)


    return app  