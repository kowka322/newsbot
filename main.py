from sources import getnews
from llm import filter_news
from delivery import send

def main():
    news = getnews()
    filtered = filter_news(news)
    send(filtered)
    

if __name__ == "__main__":
    main()