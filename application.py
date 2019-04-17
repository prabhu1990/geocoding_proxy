from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from geocoder import Geocoder

class Application(BaseHTTPRequestHandler):

    def do_GET(self):
        coordinates = self.get_coordinates()
        if coordinates is None:
            self.send_json_output(400, {'message' : 'Enter a valid address for geocoding'})
        elif coordinates is False:
            self.send_json_output(503, {'message' : 'Geocoding services are not available. Please try again later.'})
        else:
            self.send_json_output(200, coordinates)

    def get_coordinates(self):
        geocoder = Geocoder()
        uri = urlparse(self.path)
        query = parse_qs(uri.query)
        if query.get('address') is None:
            return None
        coordinates = geocoder.geocode(query['address'][0])
        return coordinates

    def send_json_output(self, status_code, coordinates):
        response_text = json.dumps(coordinates)
        self.send_response(status_code)
        self.end_headers()
        self.wfile.write(response_text.encode('utf-8'))
        return
    
