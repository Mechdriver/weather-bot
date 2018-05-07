import requests

class DarkSkyService:
    def __init__(self, api_key):
        if (not api_key):
            raise ImportError

        self.api_key = api_key

    def get_weather(self, coordinates):
        pass
