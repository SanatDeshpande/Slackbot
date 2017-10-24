import bottle as b
from bottle import Bottle
import json
import os
import socket

app = Bottle()

@app.route('/', method='POST')
def test():
    try:
        data = b.request.json
    except:
        raise Exception('Request Error')

    b.response.json = data
    return b.response.json

@app.route('/challenge', method='POST')
def answer_challenge():
    try:
        data = b.request.json
        if 'challenge' not in data:
            b.HTTPResponse.status = 400
            return
    except:
        b.HTTPResponse.status = 400
        return

    b.response.json = data
    return b.response.json['challenge']

if __name__ == '__main__':
    PORT = os.environ.get('PORT')
    HOSTNAME = socket.gethostname()
    app.run(host=HOSTNAME, port=PORT)
