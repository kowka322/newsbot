import feedparser
import re
import html


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
            items.append(
                {
                    "title": entry.title,
                    "link": entry.link,
                    "descript": clean(text),
                }
            )
    return items
