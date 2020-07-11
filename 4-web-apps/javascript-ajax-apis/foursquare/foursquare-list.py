import json
import requests

url = 'https://api.foursquare.com/v2/lists/5af879722b9844322f1aba96'

params = dict(client_id='client_id',
              client_secret='client_secret',
              v='20180528')
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)


def foursquare_list():
    # Display metadata
    print('\nResponse code: {}'.format(data['meta']['code']),
          '\nList name: {}'.format(data['response']['list']['name']),
          '\nList author: {} {}'.format(data['response']['list']['user']['firstName'],
                                        data['response']['list']['user']['lastName']),
          '\nList description: {}'.format(data['response']['list']['description']),
          '\nVenues:')
    # Iterate over list to return info for each venue
    items = data['response']['list']['listItems']['items']
    for item in items:
        print('{}, {}, {}'.format(item['venue']['name'],
                                  item['venue']['location']['address'],
                                  item['venue']['location']['city']))


# If this file is called as a standalone program:
if __name__ == '__main__':
    # Display output in terminal
    foursquare_list()
