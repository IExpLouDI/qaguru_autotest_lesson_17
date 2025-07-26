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
put = '/api/users/2'


put_body = {
    'name': 'morpheus',
    'job': 'zion resident'
}

# DELETE
delete = '/api/users/2'

headers = {
    'x-api-key': 'reqres-free-v1'
    }

# negative_headers = {
#     'free':'access'
# }
