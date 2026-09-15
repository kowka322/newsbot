from sources import getnews
from llm import filter_news
from delivery import send
from data import filter_seen

def main():
    news = getnews()
    new = filter_seen(news)
    if not new:
        send("No new news")
        return
    text = ""
    for i in new:
        text += i["title"] + "\n"
    print(text)
    filteredllm = filter_news(text)
    send(filteredllm)
    

if __name__ == "__main__":
    main()