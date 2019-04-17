# geocoding_proxy
A simple proxy service that helps find lat-long coordinates from a given street address. It depends on a couple of external services: Google & Here.



# Installation:

1. Install python3.
2. Copy secrets.json.example to secrets.json
3. Setup an account with Google Maps and add the api key to secrets.json
4. Setup an account with Here Geocoding service and add the app_id and app_code to secrets.json

# Usage:

Start the server:
```
./server.py
```

Make a request:

If you are running the service locally, you can hit the service as follows:
```
curl http://localhost:8000/?address=30%20Prince%20St,%20New%20York,%20NY%2010012
```
you should see the following output:
```
{'lat': 40.7228476, 'lng': -73.9948435}
```
