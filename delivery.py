import os

import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


def send(text):
    data = {"chat_id": CHAT_ID, "text": text}
    r = requests.post(URL, data=data)
    return r.json()["ok"]  
