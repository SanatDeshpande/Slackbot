import os
from slackclient import SlackClient
import slackeventsapi
import requests

BOT_ACCESS_TOKEN = os.environ.get("BOT_ACCESS_TOKEN")
OAUTH_ACCESS_TOKEN = os.environ.get("OAUTH_ACCESS_TOKEN")
CLIENT_ID = os.environ.get("CLIENT_ID")

sc = SlackClient(os.environ.get(BOT_ACCESS_TOKEN))

payload = {
    'token': BOT_ACCESS_TOKEN,
    'channel': '#general',
    'text': 'test'
}
results = requests.post("https://slack.com/api/chat.meMessage", params=payload)
print(results.json())
