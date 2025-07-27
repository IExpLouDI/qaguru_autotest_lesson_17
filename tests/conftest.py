import os

import pytest
import requests.adapters

from src.qaguru_autotest_lesson_17.utils.paths import SCHEMAS_DIR
from src.qaguru_autotest_lesson_17.utils.request_params import headers, url
from src.qaguru_autotest_lesson_17.utils.request_params import get, get_params, get_single
from src.qaguru_autotest_lesson_17.utils.request_params import post, post_body
from src.qaguru_autotest_lesson_17.utils.request_params import put, put_body
from src.qaguru_autotest_lesson_17.utils.request_params import delete

import requests as rq


get_not_found = pytest.mark.parametrize("get_single_user", ['/233'], indirect=True)
post_un_successful_reg = pytest.mark.parametrize("post_request", [['/api/register', {"email": "sydney@fife"}]],
                                                 indirect=True)
post_successful_reg = pytest.mark.parametrize("post_request", [['/api/register', {"email": "eve.holt@reqres.in",
                                                                                  "password": "pistol"}]
                                                               ], indirect=True)
post_reg_valid_schema = pytest.mark.parametrize('shema_path_response_type_post', ['response_schema_registr_post.json'],
                                             indirect=True)


@pytest.fixture()
def shema_path_response_type_get():
    get_shema = os.path.join(SCHEMAS_DIR, 'response_schema_get.json')
    return get_shema


@pytest.fixture(params=['response_schema_post.json'])
def shema_path_response_type_post(request):
    get_shema = os.path.join(SCHEMAS_DIR, request.param)
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
    response = session_config.get(curl, params=get_params)
    return response


@pytest.fixture(scope='function', params=[get_single])
def get_single_user(session_config, request):
    curl = url + get + request.param
    response = session_config.get(curl)
    return response


@pytest.fixture(params=[[post, post_body]])
def post_request(session_config, request):
    curl = url + request.param[0]
    response = session_config.post(curl, data=request.param[1])
    return response


@pytest.fixture()
def put_request(session_config):
    curl = url + put
    response = session_config.put(curl, data=put_body)
    return response


@pytest.fixture()
def delete_request(session_config):
    curl = url + delete
    response = session_config.delete(curl)
    return response
