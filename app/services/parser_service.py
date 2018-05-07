import re

class ParserService:
    LOCATION_GROUP_NAME = 'location'

    def __init__(self):
        self.weather_patterns = [f"what('s| is) the weather in (?P<{self.LOCATION_GROUP_NAME}>.*)",
                                 f"weather (in|at) (?P<{self.LOCATION_GROUP_NAME}>.*)",
                                 f"(?P<{self.LOCATION_GROUP_NAME}>.*) weather$"]

    def find_location_for_weather(self, message):
        formatted_message = message.lower().rstrip('?:!.,;')
        for pattern in self.weather_patterns:
            match = re.match(pattern, formatted_message)
            if (match and match.group(self.LOCATION_GROUP_NAME)):
                return match.group(self.LOCATION_GROUP_NAME)

        return None
