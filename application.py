from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from geocoder import Geocoder

class Application(BaseHTTPRequestHandler):

    def do_GET(self):
        geocoder = Geocoder()
        config = self.load_config()
        uri = urlparse(self.path)
        query = parse_qs(uri.query)
        coordinates = geocoder.geocode(config, query['address'][0])
        self.send_response(200)
        self.end_headers()
        response_text = json.dumps(coordinates)
        self.wfile.write(response_text.encode('utf-8'))
        return 0

    def load_config(self):
        config_file = open('./secrets.json', 'r')
        config_data = json.loads(config_file.read())
        config_file.close()
        return config_data
    
