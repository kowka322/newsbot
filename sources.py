import feedparser

FEEDS = ["https://feeds.feedburner.com/ign/all"]


def getnews():
    text = ""
    for url in FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            text += entry.title + "\n"
    return text




