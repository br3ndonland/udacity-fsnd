import json
import requests

url = 'https://api.foursquare.com/v2/venues/search'

params = dict(client_id='PASTE_YOUR_KEY_HERE',
    client_secret='PASTE_YOUR_KEY_HERE',
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
