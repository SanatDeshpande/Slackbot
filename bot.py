import os
from slackclient import SlackClient
import slackeventsapi
import requests
import websocket
import time

BOT_ACCESS_TOKEN = os.environ.get("BOT_ACCESS_TOKEN")
OAUTH_ACCESS_TOKEN = os.environ.get("OAUTH_ACCESS_TOKEN")
CLIENT_ID = os.environ.get("CLIENT_ID")

sc = SlackClient(os.environ.get(BOT_ACCESS_TOKEN))
url = "https://slack.com/api/rtm.connect"
payload = {
    'token': BOT_ACCESS_TOKEN
}
response = requests.post(url, params=payload)
ws = websocket.WebSocketApp(response.json()['url'])
time.sleep(5)
payload = {
    "id": 1,
    "type": "message",
    "channel": "#general",
    "text": "Hello world"
}
ws.send(data = payload)
