#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from application import Application
import json

httpd = HTTPServer(('0.0.0.0', 8000), Application)
print("Starting server at http://localhost:8000")
while True:
    httpd.handle_request()

if __name__ == '__main__':
    main()