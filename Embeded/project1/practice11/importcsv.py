from sys import argv
import csv
import sqlite3

# 커맨드 라인에서 파일명을 인자로 전달받음
if len(argv) < 2:
    print("Please provide a name of a csv file. ex: python importcsv.py myfile.csv")
    exit(1)
else:
    csvfile = argv[1]

# SQLite 데이터베이스 연결
conn = sqlite3.connect('test.db')
c = conn.cursor()

# 학생 테이블 생성
c.execute('''CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY,
                name TEXT,
                birth DATE,
                gender CHAR
            )''')

# CSV 파일에서 데이터 읽어와서 데이터베이스에 입력
with open(csvfile, 'r') as file:
    student = csv.reader(file)
    next(student)  # 첫 번째 행은 헤더이므로 건너뜀
    for index, row in enumerate(student, start=1):
        c.execute("INSERT INTO student (name, birth, gender) VALUES (?, ?, ?)", (row[0], row[1], row[2]))

# 변경사항 커밋
conn.commit()

# 연결 종료
conn.close()

print("Data imported successfully.")

