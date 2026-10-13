import feedparser
import re
import html
import time

def clean(raw):
    text = re.sub(r"<[^>]+>", " ", raw)
    text = html.unescape(text)
    return " ".join(text.split()).strip()


FEEDS = [
    "https://feeds.feedburner.com/ign/all",
    "https://www.theverge.com/rss/index.xml",
    "https://feeds.arstechnica.com/arstechnica/index",
    "https://hnrss.org/frontpage",
    "https://www.reddit.com/r/LocalLLaMA/.rss"
]


def getnews():
    items = []
    for url in FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if "content" in entry:
                text = entry["content"][0]["value"]
            else:
                text = entry.get("summary","")
            if "published_parsed" in entry:
                published_ = time.strftime("%Y-%m-%dT%H:%M:%S", entry.published_parsed)
            else:
                published_ = None

            items.append(
                {
                    "title": entry.title,
                    "link": entry.link,
                    "descript": clean(text),
                    "source": url,
                    "published": published_,
                }
            )
    return items
