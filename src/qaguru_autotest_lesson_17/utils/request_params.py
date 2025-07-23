url = 'https://reqres.in'

get = '/api/users'
post = '/api/users'
put = '/api/users/2'
delete = '/api/users/2'

post_body = {
    'name': 'morpheus',
    'job': 'leader'
}

put_body = {
    'name': 'morpheus',
    'job': 'zion resident'
}

headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'reqres-free-v1'
    }
