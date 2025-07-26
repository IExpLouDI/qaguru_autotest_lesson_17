import json

import pytest
from jsonschema import validate


@pytest.mark.positive
def test_post_status(post_request):
    assert post_request.status_code == 201


@pytest.mark.positive
def test_validate_shema_response_post(post_request, shema_path_response_type_post):
    with open(shema_path_response_type_post, 'r', encoding='utf-8') as file:
        schema = json.loads(file.read())
    validate(instance=post_request.json(), schema=schema)


@pytest.mark.positive
def test_data_in_response_post(post_request):
    data = post_request.json()
    assert data['name'] == 'tester'
    assert data['job'] == 'laos'
