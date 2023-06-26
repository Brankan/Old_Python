import requests
import sqlite3

page = requests.get("https://techniventures.com/blog/")
from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')
r = soup.find_all(class_='entry-title')
listab=[]
listlink=[]


for cos in r:
  listab.append(cos.text.strip())

for i in r:
    listlink.append(str(i.a))
listab1 = []
truelinks=[]
for x in listlink:

    page1 = requests.get(x.split('"')[1])
    truelinks.append(x.split('"')[1])
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    r1 = soup1.find_all(class_='content-area')
    for cos1 in r1:
        listab1.append(cos1.text.strip().replace("\n",""))

print(listab)
print(truelinks)
print(listab1)
ba=-1
for bff in listab1:
    ba +=1

print(ba)
create_table = """CREATE TABLE IF NOT EXISTS B
    (id INTEGER PRIMARY KEY,
    Col1 TEXT,
    Col2 TEXT,
    Col3 TEXT
);"""
db = sqlite3.connect("rp.db")

cur = db.cursor()
cur.execute(create_table)
for hg in range(ba):

    Col1, Col2, Col3=(listab[hg], truelinks[hg], listab1[hg])
    cur.execute("""INSERT INTO B
                    (Col1, Col2, Col3) VALUES (?, ?, ?)""",
                    (Col1, Col2, Col3))

cur.execute('SELECT * FROM B;')
print (cur.fetchall())

