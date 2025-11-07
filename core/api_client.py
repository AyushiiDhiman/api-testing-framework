import requests
import json
from pathlib import Path

class APIClient:
    def __init__(self):
        config_path = Path(__file__).parent.parent / "config/config.json"
        self.config = json.load(open(config_path))
        self.base_url = self.config["base_url"]
        self.timeout = self.config["timeout"]

    def get(self, endpoint, params=None):
        return requests.get(self.base_url + endpoint, params=params, timeout=self.timeout)

    def post(self, endpoint, data=None):
        return requests.post(self.base_url + endpoint, json=data, timeout=self.timeout)

    def put(self, endpoint, data=None):
        return requests.put(self.base_url + endpoint, json=data, timeout=self.timeout)

    def delete(self, endpoint):
        return requests.delete(self.base_url + endpoint, timeout=self.timeout)
