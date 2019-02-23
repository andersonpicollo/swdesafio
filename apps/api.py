# -*- coding: utf-8 -*-
from flask_restful import Api, Resource
from resources.planet import Planet


api = Api()

def configure_api(app):

    api.add_resource(Planet,"/planets", "/planets/<string:name>", "/planets/<int:planet_id>")
    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)



