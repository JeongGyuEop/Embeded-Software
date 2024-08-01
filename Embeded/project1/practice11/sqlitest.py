import sqlite3

db = sqlite3.connect('test.db')
cur = db.cursor()
query = cur.execute('SELECT * FROM student')
for row in query.fetchall():
    print(row)
cur.close()
db.close()

