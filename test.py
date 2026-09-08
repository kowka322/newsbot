import requests
import os
from dotenv import load_dotenv
from rss_test import text

load_dotenv()
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {"chat_id": CHAT_ID, "text": text}

r = requests.post(URL, data=data)
print(r.json())