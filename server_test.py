import urllib.request
import urllib.parse
import unittest
import json
from geocoder import Geocoder, GoogleService, HereService
from config import Config


coordinates_from_google = {'lat': 40.7228476, 'lng': -73.9948435}
coordinates_from_here = {'lat': 40.72291, 'lng': -73.99483}

# class ServerTest(unittest.TestCase):
#     def access_endpoint(self, path):
#         url = "http://localhost:8000{0}".format(path)
#         print(url)
#         request_handler = urllib.request.urlopen(url)
#         response_text = request_handler.read().decode('utf-8')
#         return json.loads(response_text)
    
#     def test_simple_request(self):
#         response = self.access_endpoint('/?address=30%20Prince%20St,%20New%20York,%20NY%2010012')
#         self.assertEqual(shop_coordinates, response)

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

# class GeocoderTest(unittest.TestCase):

#     def setUp(self):
#         config_file = open('./secrets.json', 'r')
#         self.config_data = json.loads(config_file.read())
#         self.geocoder = Geocoder()
#         config_file.close()

#     def test_geocoder(self):
#         address = '30 Prince St, New York, NY 10012'
#         geocoder_response = self.geocoder.geocode(self.config_data, address)
#         self.assertEqual(geocoder_response, shop_coordinates)
    
if __name__ == '__main__':
    unittest.main()
