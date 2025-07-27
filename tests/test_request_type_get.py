import json
import os.path

import pytest
from jsonschema import validate

from tests.conftest import get_not_found


@pytest.mark.positive
def test_get_positive_status_200(get_list_users):
    assert get_list_users.status_code == 200


@pytest.mark.positive
def test_validate_response_shema(get_list_users, shema_path_response_type_get):
    with open(shema_path_response_type_get, 'r', encoding='utf-8') as file:
        schema = json.loads(file.read())
    validate(instance=get_list_users.json(), schema=schema)


@pytest.mark.positive
def test_get_current_page(get_list_users):
    response_data = get_list_users.json()
    assert response_data['page'] == 1


@pytest.mark.positive
def test_get_single_user(get_single_user):
    response_data = json.loads(get_single_user.text)['data']
    assert response_data['first_name'] == 'Janet'
    assert response_data['last_name'] == 'Weaver'


@pytest.mark.negative
@get_not_found
def test_get_status_code_404(get_single_user):
    assert get_single_user.status_code == 404