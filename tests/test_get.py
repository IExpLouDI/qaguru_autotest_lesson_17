import json
import os.path

import requests as rq
from jsonschema import validate


def test_get_positive():
    url = 'https://reqres.in'
    end_point = '/api/users?page=1'
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'reqres-free-v1'
    }
    response = rq.get(url + end_point, headers=headers)
    assert response.status_code == 200
    get_shema = os.path.join('..', 'src','qaguru_autotest_lesson_17','shemas', 'response_shemas_get.json')
    with open(get_shema, 'r', encoding='utf-8') as file:
        schema = json.loads(file.read())
    validate(instance=response.json(), schema=schema)
