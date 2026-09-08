import feedparser
import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
FEEDS = ["https://feeds.feedburner.com/ign/all"]

def getnews():
    text = ""
    for url in FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            text += entry.title + "\n"
    return text

def send(text):
    data = {"chat_id": CHAT_ID, "text": text}
    r = requests.post(URL, data=data)
    print(r.json())

def main():
    news = getnews()
    send(news)
    

if __name__ == "__main__":
    main()