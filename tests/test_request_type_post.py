import json

import pytest
from jsonschema import validate

from tests.conftest import post_un_successful_reg, post_reg_valid_schema, post_successful_reg


@pytest.mark.positive
def test_post_status_201(post_request):
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


@post_un_successful_reg
def test_post_register_status_code_400(post_request):
    assert post_request.status_code == 400


@post_successful_reg
@post_reg_valid_schema
def test_post_register_valid_shema(post_request, shema_path_response_type_post):
    with open(shema_path_response_type_post, 'r', encoding='utf-8') as file:
        schema = json.loads(file.read())
    validate(instance=post_request.json(), schema=schema)
