import sqlite3
import sys

db = None
try:
    db = sqlite3.connect("test.db")
    cur = db.cursor()
    students = [
        (5, "Il JiMae", 880429, 'M'),
        (6, "Mae Chang", 810606, 'F')
    ]
    cur.executemany("INSERT INTO student(id, name, birth, gender) VALUES(?, ?, ?, ?)", students)
    db.commit()
except sqlite3.Error as e:
    # 에러 발생 시 롤백
    if db:
        db.rollback()
    print("Error %s:" % e.args[0])
    sys.exit(1)
finally:
    if db:
        db.close()

