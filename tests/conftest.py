# -*- coding: utf-8 -*-

from os.path import dirname, isfile, join
import pytest


@pytest.fixture(scope='session')
def client():
    from apps import create_app
    from apps.db import mongo

    # instancia  função factory em modo 'testing'
    flask_app = create_app('testing')

    testing_client = flask_app.test_client()

    #Criar context com as configurações
    # da aplicação
    ctx = flask_app.app_context()
    ctx.push()

    #Limpa o banco de testes
    mongo.db.planets.drop()

    # retorna o client criado
    yield testing_client

    # remove o contexto ao terminar os testes
    ctx.pop()


@pytest.fixture(scope='function')
def mongo(request, client):

    def fin():
        from resources.planet import Planet
        Planet.objects.all().delete()
        print('\n[teardown] disconnect from db')

    fin()