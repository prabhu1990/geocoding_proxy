import json

class Config:
    def __init__(self):
        config_file = open('./secrets.json')
        self.config_data = json.loads(config_file.read())
        config_file.close()
