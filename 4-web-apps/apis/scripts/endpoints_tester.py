import requests
import sys

print('Running Endpoint Tester...\n')
address = input('Please enter the address of the server you want to access.'
    "\nIf left blank the connection will be set to 'http://localhost:5000': ")
if address == '':
    address = 'http://localhost:5000'
# Making a GET Request
print('Making a GET Request for /puppies...')
try:
    url = '{}/puppies'.format(address)
    r = requests.get(url=url)
    if r.status_code != 200:
        raise Exception(
            'Received a status code of {}'.format(r.status_code))
except Exception as err:
    print('Test 1 FAILED: Could not make GET Request to web server')
    print(err.args)
    sys.exit()
else:
    print('Test 1 PASS: Succesfully Made GET Request to /puppies')

# Making GET Requests to /puppies/id
print('Making GET requests to /puppies/id')
try:
    id = 1
    while id <= 10:
        url = '{}/puppies/{}'.format(address, id)
        r = requests.get(url=url)
        if r.status_code != 200:
            raise Exception(
                'Received a status code of {}'.format(r.status_code))
        id = id + 1
except Exception as err:
    print('Test 2 FAILED: Could not GET /puppies/{}'.format(id)')
    print(err.args)
    sys.exit()
else:
    print('Test 2 PASS: Succesful GET request to /puppies/{}'.format(id))
    print('ALL TESTS PASSED!!')
