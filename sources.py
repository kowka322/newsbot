import feedparser
import re
import html

def clean(raw):
    text = re.sub(r"<[^>]+>", " ", raw)
    text = html.unescape(text)
    return " ".join(text.split()).strip()



FEEDS = [ "https://feeds.feedburner.com/ign/all",
            "https://www.theverge.com/rss/index.xml",
            "https://feeds.arstechnica.com/arstechnica/index",
            "https://hnrss.org/frontpage",
            "https://www.reddit.com/r/LivestreamFail/.rss",
            "https://www.reddit.com/r/SubredditDrama/.rss",
            "https://www.reddit.com/r/LocalLLaMA/.rss",
            "https://www.youtube.com/feeds/videos.xml?channel_id=UCq6VFHwMzcMXbuKyG7SQYIg"
        ]


def getnews():
    items = []
    for url in FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            items.append({"title": entry.title, "link": entry.link, "descript": clean(entry.get("summary", ""))})
    return items

