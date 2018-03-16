import json
import requests

url = 'https://api.foursquare.com/v2/venues/search'

params = dict(client_id='5JU1MJJJ4OUU2OQO1XYMMGK5OOHBCF3FFJURKWGXIIM0AN0Q',
    client_secret='BJ5QE50VMWVRFEZBNQO3O4RBFJDPFCNZ0P13GUDERTAG054Y',
    v='20180309',
    ll='37.392971,-122.076044',
    query='pizza',
    limit=1)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

# If this file is called as a standalone program:
if __name__ == '__main__':
    # Run a sample location for debugging
    print('Venue name: {}'.format(data['response']['venues'][0]['name']))
