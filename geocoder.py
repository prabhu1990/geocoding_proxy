import urllib.request
import urllib.parse
import json
from config import Config

class Geocoder:
    def __init__(self):
        self.config = Config().config_data
    
    def geocode(self, address):
        google_service = GoogleService(self.config, address)
        here_service = HereService(self.config, address)
        
        result = google_service.geocode()
        if result == False:
            result = here_service.geocode()
        return result

class GeocodingService:    
    base_url = "undefined"
    def __init__(self, config, address):
        self.config = config
        self.address = address

    def params(self):
        pass

    def parse_results(self, text):
        pass

    def geocode(self):
        url = "{}?{}".format(self.base_url, urllib.parse.urlencode(self.params()))
        try:
            response = urllib.request.urlopen(url)
        except urllib.request.URLError as e:
            return False
        else:
            response_text = response.read().decode('utf-8')
            return self.parse_results(response_text)
    
class GoogleService(GeocodingService):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    def params(self):
        return {
            'address' : self.address,
            'key' : self.config['google']['api_key']
        }
    
    def parse_results(self, text):
        data = json.loads(text)
        coordinates = data['results'][0]['geometry']['location']
        return coordinates

class HereService(GeocodingService):
    base_url = "https://geocoder.api.here.com/6.2/geocode.json"

    def params(self):
        return {
            'app_id' : self.config['here']['app_id'],
            'app_code' : self.config['here']['app_code'],
            'searchtext' : self.address
        }
    
    def parse_results(self, text):
        data = json.loads(text)
        coordinates = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']
        return {
            'lat' : coordinates['Latitude'],
            'lng' : coordinates['Longitude']
        }
    


