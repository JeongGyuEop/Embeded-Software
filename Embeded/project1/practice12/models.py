from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250))
    datetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Schedule {self.title}>"

