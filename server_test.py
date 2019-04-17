import urllib.request
import urllib.parse
import unittest
import json
from geocoder import Geocoder, GoogleService, HereService
from config import Config

coordinates_from_google = {'lat': 40.7228476, 'lng': -73.9948435}
coordinates_from_here = {'lat': 40.72291, 'lng': -73.99483}

class IntegrationTest(unittest.TestCase):
    def access_endpoint(self, path):
        url = "http://localhost:8000{0}".format(path)
        try:
            response = urllib.request.urlopen(url)
        except urllib.request.URLError as e:
            return e.code, None
        else:
            response_text = response.read().decode('utf-8')
            return response.getcode(), json.loads(response_text)

    def test_good_request(self):
        status_code, response = self.access_endpoint('/?address=30%20Prince%20St,%20New%20York,%20NY%2010012')
        self.assertEqual(status_code, 200)
        self.assertEqual(coordinates_from_google, response)

    def test_bad_request(self):
        status_code, response = self.access_endpoint('/')
        self.assertEqual(status_code, 400)

class HereGeocodingTest(unittest.TestCase):
    def test_request(self):
        address = '30 Prince St, New York, NY 10012'
        config = Config().config_data
        coordinates = HereService(config, address).geocode()
        self.assertEqual(coordinates_from_here, coordinates)

class GoogleGeocodingTest(unittest.TestCase):
    def test_request(self):
        address = '30 Prince St, New York, NY 10012'
        config = Config().config_data
        coordinates = GoogleService(config, address).geocode()
        self.assertEqual(coordinates_from_google, coordinates)

if __name__ == '__main__':
    unittest.main()
