import bottle as b
from bottle import Bottle
import json
import os
import socket
import logging
import sys
import requests

app = Bottle()

@app.route('/', method='POST')
def test():
    try:
        data = b.request.json
    except:
        raise Exception('Request Error')

    b.response.json = data
    print(data)
    return b.response.json

@app.route('/event', method='POST')
def handle_event():
    #handles initial challenge
    try:
        data = b.request.json
        print('checkpoint 1')
        if 'challenge' in data:
            return data['challenge']
        print('checkpoint 2')
    except:
        b.HTTPResponse.status = 400
        return
    #handling of actual event
    payload = {
        'token': data['token'],
        'text': 'response',
        'channel': data['event']['channel']
    }
    print(payload)
    results = requests.post("https://slack.com/api/chat.meMessage", params=payload)
    return data

if __name__ == '__main__':
    PORT = os.environ.get('PORT')
    HOSTNAME = socket.gethostname()
    if len(sys.argv) == 2 and sys.argv[1] == 'debug':
        PORT = '8080'
        HOSTNAME = '127.0.0.1'
    app.run(host=HOSTNAME, port=PORT)
