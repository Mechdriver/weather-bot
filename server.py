from flask import Flask, request
from flask_cors import CORS

import json
import sys

JOIN_ACTION = 'join'
MESSAGE_ACTION = 'message'

app = Flask(__name__)
CORS(app)

@app.route("/chat/messages", methods=['POST'])
def response_to_message():
    response_dict = {'messages': []}
    payload_dict = request.form
    action = payload_dict['action']

    if (action == JOIN_ACTION):
        message = 'Hello, ' + payload_dict['name'] + '!'
        message_dict = {'type': 'text', 'text': message}
        response_dict['messages'].append(message_dict)

        return json.dumps(response_dict), 200, {'ContentType':'application/json'}

    elif (action == MESSAGE_ACTION):
        response_dict = {'messages': [{'type': 'text', 'text': payload_dict['text']}]}

    #print(payload_dict, file=sys.stderr)

    return json.dumps(response_dict), 200, {'ContentType':'application/json'}

if __name__=='__main__':
    app.run(debug=True, port=9000)
