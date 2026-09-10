import sqlite3  
from sources import getnews



def filter_seen(items):
    conn = sqlite3.connect("seen.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS seen (link TEXT PRIMARY KEY)")
    new = []
    for item in items:
        link = item["link"]
        cur.execute("SELECT 1 FROM seen WHERE link = ?", (link,))
        result = cur.fetchone()
        if result == None:
            new.append(item)
            cur.execute("INSERT OR IGNORE INTO seen (link) VALUES (?)", (link,))
    conn.commit()
    return new
    
if __name__ == "__main__":
    print(filter_seen(getnews()))