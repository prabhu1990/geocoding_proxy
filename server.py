#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        response_text = json.dumps({'key' : 'xyzxyz'})
        self.wfile.write(response_text.encode('utf-8'))
        return

httpd = HTTPServer(('0.0.0.0', 8000), RequestHandler)
print("Starting server at http://localhost:8000")
while True:
    httpd.handle_request()

if __name__ == '__main__':
    main()