# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
import json
from bson.objectid import ObjectId
from apps.db import mongo

class Planet(Resource):
  
    
    def get(self,name=None,planet_id=None):

        try:
            if name:
                planet = mongo.db.planets.find_one({"name": name})
                if planet:
                    return jsonify(planet)
                else:
                    return jsonify({"response":"Not found"})
            
            elif planet_id:
                planet = mongo.db.planets.find_one({"_id": planet_id})
                if planet:
                    return jsonify(planet)
                else:
                  return jsonify({"response":"Not found"})  
            else:
                planets = []
                planets_db = mongo.db.planets.find({})
                for planet in planets_db:
                    planets.append(planet)
                return jsonify(planets)
            
        except Exception as a:
                    return {"response":"Exception{}".format(a)}

        return jsonify({"response":"Not found"})     
                          

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('name',type=str)
        parser.add_argument('climate',type=str)
        parser.add_argument('terrain',type=str)
        args = parser.parse_args()

        if not args:
            data = {"response": "ERROR"}
            return jsonify(data)
        else:
            planet = {
                "_id": hash(args['name']),
                "name": args['name'],
                "climate" : args['climate'],
                "terrain" : args['terrain']
            }

            if args['name']:
                try:
                    if mongo.db.planets.find_one({"name": planet['name']}):
                        return jsonify({"response": "planet already exists."})
                    else:
                        mongo.db.planets.insert(planet)
                except Exception as e:
                    return jsonify({"response":"an erro occurred - {}".format(e)})
                
            else:
                return jsonify({"response": "planet missing"})
        
        return jsonify({"response": "save"})

    def delete(self,name):

        if not name:
            data = {"response","ERROR"}
            return jsonify(data)
        else:
            try:                
                if not mongo.db.planets.find_one({"name": name}):
                    return {"response": "planet does not exist"}
                else:
                    mongo.db.planets.remove({'name': name})
                    return jsonify({"response":"{} successfully removed".format(name)})
            except Exception as e:
                return jsonify({"response:ERROR: - {}".format(e)})

        
        