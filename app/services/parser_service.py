import re

class ParserService:
    def __init__(self):
        self.weather_patterns = ["what's the weather in (.*)",
                                 "weather in (.*)",
                                 "(.*) weather$"]

    def find_location_for_weather(self, message):
        formatted_message = message.lower().rstrip('?:!.,;')
        for pattern in self.weather_patterns:
            match = re.match(pattern, formatted_message)
            if (match and match.group(1)):
                return match.group(1)

        return None
