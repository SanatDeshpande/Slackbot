import bottle as b
from bottle import Bottle
import json
import os
import socket
import logging

app = Bottle()

@app.route('/', method='POST')
def test():
    try:
        data = b.request.json
    except:
        raise Exception('Request Error')

    b.response.json = data
    logging.warning(data)
    return b.response.json

@app.route('/event', method='POST')
def handle_event():
    #handles initial challenge
    try:
        data = b.request.json
        if 'challenge' in data:
            return data['challenge']
    except:
        b.HTTPResponse.status = 400
        return
    #handling of actual event
    print(data)
    b.HTTPResponse.status = 200
    return b.HTTPResponse.status

if __name__ == '__main__':
    PORT = os.environ.get('PORT')
    HOSTNAME = socket.gethostname()
    if PORT is None:
        PORT = '8080'
    if 'local' in HOSTNAME:
        HOSTNAME = '127.0.0.1'
    app.run(host=HOSTNAME, port=PORT)
