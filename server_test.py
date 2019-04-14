import urllib.request
import urllib.parse
import unittest
import json


class ServerTestCase(unittest.TestCase):
    def access_endpoint(self, path):
        url = "http://localhost:8000{0}".format(path)
        request_handler = urllib.request.urlopen(url)
        response_text = request_handler.read().decode('utf-8')
        return json.loads(response_text)
    
    def test_simple_request(self):
        self.assertEqual(self.access_endpoint('/'), {'key' : 'xyzxyz'})
    
if __name__ == '__main__':
    unittest.main()
