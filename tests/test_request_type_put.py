import json

import pytest
from jsonschema import validate


@pytest.mark.positive
def test_validate_shema_response_put(put_request, shema_path_response_type_put):
    with open(shema_path_response_type_put, 'r', encoding='utf-8') as file:
        schema = json.loads(file.read())
    validate(instance=put_request.json(), schema=schema)


@pytest.mark.positive
def test_data_in_response_put(put_request):
    data = put_request.json()
    assert data['name'] == 'zendeus'
    assert data['job'] == 'customer'
