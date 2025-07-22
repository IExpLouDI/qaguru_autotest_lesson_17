import requests as rq


def test_simple_request():
    url = 'https://reqres.in'
    end_point = '/api/users?page=1'
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'reqres-free-v1'
    }
    response = rq.get(url + end_point, headers=headers)
    assert response.status_code == 200
    print()
