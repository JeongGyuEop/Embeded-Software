from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# create_engine으로부터 엔진을 생성합니다.
engine = create_engine('sqlite:///test.db')

# sessionmaker를 사용하여 세션 클래스를 생성합니다.
Session = sessionmaker(bind=engine)

# 세션 객체를 생성합니다.
db_session = Session()

# 나머지 코드는 변하지 않습니다.
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

class Student(Base):
    __tablename__ = 'Student'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    birth = Column(String)
    gender = Column(String)

    def __init__(self, id=1, name=None, birth=None, gender=None):
        self.id = id
        self.name = name
        self.birth = birth
        self.gender = gender

    def __repr__(self):
        return '<%r, %r, %r>' % (self.name, self.birth, self.gender)

def show():
    # ORM을 사용하여 데이터를 가져옵니다.
    students = db_session.query(Student).all()
    for student in students:
        print(student)

def show_all():
    # ORM을 사용하여 데이터를 가져옵니다.
    students = db_session.query(Student).all()
    print(students)

def show_item(item):
    # ORM을 사용하여 데이터를 가져옵니다.
    students = db_session.query(Student).filter(Student.name.like(f'%{item}%')).all()
    print(students)

