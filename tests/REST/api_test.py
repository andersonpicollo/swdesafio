# -*- coding: utf-8 -*-

import json
def fake_planet():
    return {
                "name":"Ojom", 
                 "climate":"frigid",
                 "terrain":"oceans, glaciers"
            }

# O `client` é uma fixture em conftest.py

#POST
def test_planet_save(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    fake = fake_planet()
    url  = "/planets"
    response = client.post(url, data=json.dumps(fake), headers=headers)
    result = json.loads(response.data.decode('utf-8'))
    assert response.content_type == mimetype
    assert result['response'] == 'save'

def test_planet_exists(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }

    fake = fake_planet()
    url  = "/planets"
    response = client.post(url, data=json.dumps(fake), headers=headers)
    result = json.loads(response.data.decode('utf-8'))
    assert response.content_type == mimetype
    assert result['response'] == 'planet already exists.'

#GET
def test_get_200(client):
    response = client.get('/planets')
    assert response.status_code == 200

def test_get_planet(client):
    fake = fake_planet()
    url  = "/planets/{}".format(fake['name'])   
    response = client.get(url)
    data = json.loads(response.data.decode('utf-8'))
    assert data['name'] == fake['name']

def test_get_planet_list(client):
    fake = fake_planet()
    url  = "/planets/{}".format(fake['name']) 
    response = client.get(url)
    planet = json.loads(response.data.decode('utf-8'))
    
    response = client.get('planets')
    data = json.loads(response.data.decode('utf-8'))

    assert planet in data    
    
    

