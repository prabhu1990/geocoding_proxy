import urllib.request
import urllib.parse
import json

class Geocoder:
    def __init__(self):
        pass
    
    def geocode(self, config, address):
        params = {}
        params['address'] = address
        google_config = config['google']
        if google_config and google_config['api_key']:
            params['key'] = google_config['api_key']
        url_endpoint = 'https://maps.googleapis.com/maps/api/geocode/json'
        url = '{0}?address={1}'.format(url_endpoint, urllib.parse.urlencode(params))
        request_handler = urllib.request.urlopen(url)
        response_body = request_handler.read().decode('utf-8')
        response = json.loads(response_body)
        coordinates = response['results'][0]['geometry']['location']
        return coordinates


