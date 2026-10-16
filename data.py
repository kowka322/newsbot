import sqlite3  
from sources import getnews
from datetime import datetime, timezone



def filter_seen(items):
    conn = sqlite3.connect("seen.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS articles (link TEXT PRIMARY KEY, title TEXT, text TEXT, source TEXT, published TEXT, time TEXT, llm_pass INTEGER, sent INTEGER)")
    new = []
    for item in items:
        link = item["link"]
        title = item["title"]
        text = item["descript"]
        time_ = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
        source = item["source"]
        published = item["published"]
        cur.execute("SELECT 1 FROM articles WHERE link = ? AND llm_pass IS NOT NULL", (link,))
        result = cur.fetchone()
        if result == None:
            new.append(item)
            cur.execute("INSERT OR IGNORE INTO articles (link, title, text, time, source, published) VALUES (?,?,?,?,?,?)", (link,title,text,time_,source,published))
    conn.commit()
    return new


def llmpass(new,kept):
    conn = sqlite3.connect("seen.db")
    cur = conn.cursor()
    for item in new:
        link = item["link"]
        if item in kept:
            llm_pass = True 
        else:
            llm_pass = False
        cur.execute("UPDATE OR IGNORE articles SET llm_pass = ? WHERE link = ?", (llm_pass, link))
    conn.commit()
    
if __name__ == "__main__":
    print(filter_seen(getnews()))