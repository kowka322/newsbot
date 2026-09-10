import feedparser

FEEDS = ["https://feeds.feedburner.com/ign/all"]


def getnews():
    items = []
    for url in FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            items.append({"title": entry.title, "link": entry.link})
    return items


