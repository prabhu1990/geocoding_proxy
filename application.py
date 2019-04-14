from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class Application(BaseHTTPRequestHandler):
    def do_GET(self):
        uri = urlparse(self.path)
        query = parse_qs(uri.query)
        self.send_response(200)
        self.end_headers()
        response_text = json.dumps(query)
        self.wfile.write(response_text.encode('utf-8'))
        return
    
