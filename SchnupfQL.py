#!venv/bin/python3

import requests
import sqlite3
import sys
from bs4 import BeautifulSoup

url = 'http://www.schnupfspruch.ch/sprueche_view.asp?MOVE={}&PrevPage=1' 

# create db
conn = sqlite3.connect('spruechli.db')
c = conn.cursor()
c.execute("""
        CREATE TABLE spruechli (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titel TEXT,
            inhalt TEXT
        );""")
conn.commit()

# download pages and insert into db
for i in range(1, 110):
    sys.stdout.write('.')
    sys.stdout.flush()
    r = requests.get(url.format(i))
    soup = BeautifulSoup(r.text, 'html.parser')
    ss = soup.find_all('pre')
    for s in ss:
        content = s.text
        title = s.parent.parent.previous_sibling.previous_sibling.td.b.text
        c.execute(f"""
            INSERT INTO spruechli (titel, inhalt)
            VALUES ("{title}", "{content}");""")            
    conn.commit()
    
conn.close()

