import pytest
import json
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from server import app_factory

def test_get1_method_succes(test_client):
    
    response = test_client.get('/')
    assert response.status_code == 200
# add work
# curl -i -H "Content-Type: application/json" -X POST -d '{"link":"Yisca Kablan", "desc":"Yisca Kablan", "date":"10/20/20" ,"Subject":"Jerusalem"}' http://3.19.155.223/action

# curl -i -H "Content-Type: application/json" -X POST -d '{"_id":"61f36ac505d9c6130e174809"}' http://3.19.155.223/remove/


