# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_restful import Resource
import json
from bson.objectid import ObjectId
from apps.db import mongo

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return obj

class PlanetList(Resource):
    
    def get(self):
        planets = []
        
        try:
            data = mongo.db.planets.find({})
            for planet in data:
                planets.append(planet)
            return json.dumps(planets, cls=Encoder)
            
        except Exception as e:
            return jsonify({"reponse":"ERROR: - {}".format(e)})          
