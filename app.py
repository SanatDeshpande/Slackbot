import bottle as b
from bottle import Bottle
import json

app = Bottle()

@app.route('/', method='POST')
def test():
    try:
        data = b.request.json
        if 'key' not in data:
            raise Exception('Key not found')
    except:
        raise Exception('Request Error')

    key = data['key']
    b.response.json = {'key': key}
    return b.response.json

app.run(host='127.0.0.1', port=8080)
