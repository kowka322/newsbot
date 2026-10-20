import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


def send(text):
    buttons = {"inline_keyboard": [[{
        "text": "I like it", "callback_data": "1"
    },
    {
        "text": "I don't like it", "callback_data": "0"
    }
    ]]}    
    data = {"chat_id": CHAT_ID, "text": text, "reply_markup": json.dumps(buttons)}
    r = requests.post(URL, data=data)
    answer = r.json()
    if answer["ok"] == True:
        return answer["result"]["message_id"]
    return None
