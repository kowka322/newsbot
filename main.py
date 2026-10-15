from sources import getnews
from llm import filter_news, summarize
from delivery import send
from data import filter_seen, llmpass


def main():
    news = getnews()
    new = filter_seen(news)
    if not new:
        send("No new news")
        return
    filtered = filter_news(new)
    llmpass(new, filtered)
    for item in filtered:
        summary = summarize(item["descript"])
        msg = f"{item['title']}\n\n{summary}\n\n{item['link']}"
        send(msg)
    

if __name__ == "__main__":
    main()