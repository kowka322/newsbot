import sqlite3  
from sources import getnews
from datetime import datetime




def filter_seen(items):
    conn = sqlite3.connect("seen.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS articles (link TEXT PRIMARY KEY, title TEXT, text TEXT, source TEXT, published TEXT, time TEXT, llm_pass INTEGER)")
    new = []
    for item in items:
        link = item["link"]
        title = item["title"]
        text = item["descript"]
        time_ = datetime.now().isoformat(timespec="seconds")
        source = item["source"]
        published = item["published"]
        #llm_pass =
        cur.execute("SELECT 1 FROM articles WHERE link = ?", (link,))
        result = cur.fetchone()
        if result == None:
            new.append(item)
            cur.execute("INSERT OR IGNORE INTO articles (link, title, text, time, source, published) VALUES (?,?,?,?,?,?)", (link,title,text,time_,source,published))

    conn.commit()
    return new
    
if __name__ == "__main__":
    print(filter_seen(getnews()))