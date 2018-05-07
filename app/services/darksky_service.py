import requests

class DarkSkyService:
    FORECAST_ENDPOINT = 'https://api.darksky.net/forecast/'

    def __init__(self, api_key):
        if (not api_key):
            raise ImportError

        self.api_key = api_key

    def get_weather(self, coordinates):
        lat = coordinates['lat']
        lng = coordinates['lng']

        results = requests.get(self.FORECAST_ENDPOINT + f'{self.api_key}/{lat},{lng}' )

        if (results.status_code != 200):
            return None

        forecast_dict = results.json()

        current_dict = forecast_dict['currently']
        temperature = str(round(current_dict['temperature']))
        summary = current_dict['summary']
        # e.g. 48F. Rain
        return f'{temperature}F. {summary}'
