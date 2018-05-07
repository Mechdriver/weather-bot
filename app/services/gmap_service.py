import requests

class GMapService:
    GEOCODE_ENDPOINT = 'https://maps.googleapis.com/maps/api/geocode/json'

    def __init__(self, api_key):
        if (not api_key):
            raise ImportError

        self.api_key = api_key

    #Returns the latitude and longitude in a dictionary
    def get_coordinates(self, location):
        payload = {'address': location, 'key': self.api_key}
        results = requests.get(self.GEOCODE_ENDPOINT, params=payload)

        gmap_dict = results.json()

        if (not gmap_dict['results']):
            return None

        return gmap_dict['results'][0]['geometry']['location']
