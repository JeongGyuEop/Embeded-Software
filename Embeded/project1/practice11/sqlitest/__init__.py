from flask import Flask, request, url_for, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/user/Desktop/Embeded-Software/project1/practice11/test.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    birth = db.Column(db.String)
    gender = db.Column(db.String)

    def __init__(self, id=1, name=None, birth=None, gender=None):
        self.id = id
        self.name = name
        self.birth = birth
        self.gender = gender

    def __repr__(self):
        return '<%r, %r, %r>' % (self.name, self.birth, self.gender)

@app.route('/show')
def show():
    row = db.session.query(Student).all()
    if row:
        return render_template('showitem.html', items=row)
    return abort(404, "Page not found")

@app.route('/show/<item>')
def showitem(item):
    row = db.session.query(Student).filter(Student.name.like("%" + item + "%")).all()
    print(row)
    if row:
        return render_template('showitem.html', items=row)
    return abort(404, "Page not found")

