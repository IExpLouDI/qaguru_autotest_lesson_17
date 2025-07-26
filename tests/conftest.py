import os

import pytest
import requests.adapters

from src.qaguru_autotest_lesson_17.utils.paths import SCHEMAS_DIR
from src.qaguru_autotest_lesson_17.utils.request_params import headers, url
from src.qaguru_autotest_lesson_17.utils.request_params import get, get_params, get_single
from src.qaguru_autotest_lesson_17.utils.request_params import post, post_body
import requests as rq


@pytest.fixture()
def shema_path_response_type_get():
    get_shema = os.path.join(SCHEMAS_DIR, 'response_schema_get.json')
    return get_shema


@pytest.fixture()
def shema_path_response_type_post():
    get_shema = os.path.join(SCHEMAS_DIR, 'response_schema_post.json')
    return get_shema


@pytest.fixture(scope='session')
def session_config():
    session = rq.sessions.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=3)
    session.mount(prefix='https://', adapter=adapter)
    session.headers = headers

    with session as s:
        yield s

    print('Exit session')


@pytest.fixture(scope='session')
def get_list_users(session_config):
    curl = url + get
    response = session_config.get(curl, headers=headers, params=get_params)
    return response


@pytest.fixture(scope='function', params=[get_single])
def get_single_user(session_config, request):
    curl = url + get + request.param
    response = session_config.get(curl)
    return response

get_not_found = pytest.mark.parametrize("get_single_user", ['/233'], indirect=True)

@pytest.fixture()
def post_request(session_config):
    curl = url + post
    response = session_config.post(curl, data=post_body, headers=headers)
    return response
