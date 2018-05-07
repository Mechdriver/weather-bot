from flask import Flask, request
from flask_cors import CORS
from services.gmap_service import GMapService
from services.darksky_service import DarkSkyService
from services.parser_service import ParserService

import json, sys, os

JOIN_ACTION = 'join'
MESSAGE_ACTION = 'message'

app = Flask(__name__)
CORS(app)

parser_service = ParserService()

try:
    gmap_service = GMapService(os.environ.get('GMAP_KEY'))
except ImportError:
    error_message = 'Please supply an API key for Google Maps'
    print(error_message, file=sys.stderr)
    exit()

try:
    dark_sky_service = DarkSkyService(os.environ.get('DARKSKY_KEY'))
except ImportError:
    error_message = 'Please supply an API key for Dark Sky'
    print(error_message, file=sys.stderr)
    exit()


@app.route("/chat/messages", methods=['POST'])
def response_to_message():
    response_dict = {'messages': []}
    payload_dict = request.form
    action = payload_dict['action']

    if (action == JOIN_ACTION):
        user_name = payload_dict['name']
        message = f"Hello, {user_name}!"
        message_dict = {'type': 'text', 'text': message}

    elif (action == MESSAGE_ACTION):
        message = 'Sorry. I could not find the weather there!'
        location = parser_service.weather_find_location(payload_dict['text'])
        coords = weather = None

        if (location):
            coords = gmap_service.get_coordinates(location)

        if (coords):
            weather = dark_sky_service.get_weather(coords)

        if (weather):
            message = f"Currently it's {weather}"

        message_dict = {'type': 'text', 'text': message}

    response_dict['messages'].append(message_dict)
    return json.dumps(response_dict), 200, {'ContentType':'application/json'}

if __name__=='__main__':
    app.run(debug=True, port=9000)
