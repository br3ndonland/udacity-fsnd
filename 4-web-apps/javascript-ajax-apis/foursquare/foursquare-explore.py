import json
import requests

url = 'https://api.foursquare.com/v2/venues/search'

params = dict(client_id='PASTE_YOUR_KEY_HERE',
              client_secret='PASTE_YOUR_SECRET_HERE',
              v='20180323',
              ll='42.3495694,-71.0836727',
              query='george howell',
              limit=1)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

# If this file is called as a standalone program:
if __name__ == '__main__':
    # Run a sample location for debugging
    print(data)
    print('\n Venue name: {} \n Venue address: {}'
          .format(data['response']['venues'][0]['name'],
                  data['response']['venues'][0]['location']['address']))
