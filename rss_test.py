import feedparser
URL = "https://feeds.feedburner.com/ign/all"

feed = feedparser.parse(URL)


text = ""
for entry in feed.entries:
    text += entry.title + "\n"
    

