#!/usr/bin/env python3

# Udacity FSND API mashup

import json
import requests
from geocode import get_geocode_location

# render non-ascii characters properly in code
# import sys
# import codecs
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
# sys.stderr = codecs.getwriter('utf8')(sys.stderr)

# Store Foursquare credentials
foursquare_client_id = 'foursquare_client_id'
foursquare_client_secret = 'foursquare_client_secret'


def find_a_restaurant(mealType, location):
    """Locate a restaurant and image based on type of food and location."""
    # 1. Get latitude and longitude of location from Google Maps API
    latitude, longitude = get_geocode_location(location)
    coordinates = '{},{}'.format(latitude, longitude)
    # 2. Find restaurant with Foursquare API
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        client_id=foursquare_client_id,
        client_secret=foursquare_client_secret,
        v='20180310',
        ll=coordinates,
        query='mealType')
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    # 3. If there is a response, retrieve first restaurant
    if data['response']['venues']:
        restaurant = data['response']['venues'][0]
        venue_id = restaurant['id']
        restaurant_name = restaurant['name']
        restaurant_address = restaurant['location']['formattedAddress']
        address = ''
        for i in restaurant_address:
            address += i + ' '
        restaurant_address = address
        # 4. Find images of restaurant with Foursquare API using venue_id
        url = 'https://api.foursquare.com/v2/venues/{}/photos'.format(venue_id)
        params = dict(
            client_id=foursquare_client_id,
            client_secret=foursquare_client_secret,
            v='20180310')
        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)
        # 5. Retrieve 300 x 300 px image
        if data['response']['photos']['items']:
            firstpic = data['response']['photos']['items'][0]
            prefix = firstpic['prefix']
            suffix = firstpic['suffix']
            image_url = prefix + '300x300' + suffix
        else:
            # 6. Provide fallback image if restaurant image is not available
            image_url = 'https://picsum.photos/300/300/?random'
        # 7. Return dict containing restaurant name, address, and image url
        restaurant_info = {
            'name': restaurant_name,
            'address': restaurant_address,
            'image': image_url}
        # 8. Print results
        print('Restaurant Name: {} \n'.format(restaurant_info['name']),
            'Restaurant Address: {} \n'.format(restaurant_info['address']),
            'Image URL: {} \n'.format(restaurant_info['image']))
        return restaurant_info
    else:
        print('No restaurants found for {}. \n'.format(location))
        return 'No restaurants found'


# If this file is called as a standalone program:
if __name__ == '__main__':
    # Run the following queries:
    print('Queries for Udacity lesson \n')
    find_a_restaurant('Pizza', 'Tokyo, Japan')
    find_a_restaurant('Tacos', 'Jakarta, Indonesia')
    find_a_restaurant('Tapas', 'Maputo, Mozambique')
    find_a_restaurant('Falafel', 'Cairo, Egypt')
    find_a_restaurant('Spaghetti', 'New Delhi, India')
    find_a_restaurant('Cappuccino', 'Geneva, Switzerland')
    find_a_restaurant('Sushi', 'Los Angeles, California')
    find_a_restaurant('Steak', 'La Paz, Bolivia')
    find_a_restaurant('Gyros', 'Sydney, Australia')
