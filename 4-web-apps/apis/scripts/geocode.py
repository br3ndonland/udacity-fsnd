#!/usr/bin/env python3

import json
import requests

google_api_key = 'google_api_key'


def get_geocode_location(input_string):
    """Retrieve latitude and longitude coordinates from Google Maps."""
    location_string = input_string.replace(' ', '+')
    url = (
        'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
        .format(location_string, google_api_key))
    resp = requests.get(url=url)
    result = json.loads(resp.text)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return latitude, longitude


# If this file is called as a standalone program:
if __name__ == '__main__':
    # Run a sample location for debugging
    sample_location = input('Please enter a sample location: ')
    sample_coordinates = get_geocode_location(sample_location)
    print('Sample location: {}'.format(sample_location),
          '\n', 'Coordinates: {}'.format(sample_coordinates))
