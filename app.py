import bottle as b
from bottle import Bottle
import json
import os
import socket

app = Bottle()

@app.route('/', method='POST')
def return_key():
    try:
        data = b.request.json
        if 'key' not in data:
            raise Exception('Key not found')
    except:
        raise Exception('Request Error')

    key = data['key']
    b.response.json = {'key': key}
    return b.response.json


if __name__ == '__main__':
    PORT = os.environ.get('PORT')
    HOSTNAME = socket.gethostname()
    app.run(host=HOSTNAME, port=PORT)
