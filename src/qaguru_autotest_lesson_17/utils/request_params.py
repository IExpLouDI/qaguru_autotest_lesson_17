url = 'https://reqres.in'

# GET
get = '/api/users'
get_params = {'page': "1"}
get_single = '/2'

# POST
post = '/api/users'

post_body = {
    'name': 'tester',
    'job': 'laos'
}

# PUT
put = '/api/users/7'


put_body = {
    'name': 'zendeus',
    'job': 'customer'
}

# DELETE
delete = '/api/users/2'

#HEADERS
headers = {
    'x-api-key': 'reqres-free-v1'
    }