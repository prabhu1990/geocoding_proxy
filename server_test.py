import urllib.request
import urllib.parse
import unittest
import json


class ServerTestCase(unittest.TestCase):
    def access_endpoint(self, path):
        url = "http://localhost:8000{0}".format(path)
        print(url)
        request_handler = urllib.request.urlopen(url)
        response_text = request_handler.read().decode('utf-8')
        return json.loads(response_text)
    
    def test_simple_request(self):
        response = self.access_endpoint('/?address=30%20Prince%20St,%20New%20York,%20NY%2010012')
        self.assertEqual({'address' : ['30 Prince St, New York, NY 10012']}, response)

    
if __name__ == '__main__':
    unittest.main()
