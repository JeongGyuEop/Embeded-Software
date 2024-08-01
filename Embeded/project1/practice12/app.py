from flask import render_template
from flask import Flask, request, jsonify
from models import db, Schedule
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedule.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 홈페이지 및 스케줄 목록 라우트
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# 스케줄 생성
@app.route('/schedules', methods=['POST'])
def create_schedule():
    data = request.get_json()
    schedule = Schedule(
        title=data['title'],
        description=data.get('description'),
        datetime=datetime.strptime(data['datetime'], '%Y-%m-%d %H:%M:%S')
    )
    db.session.add(schedule)
    db.session.commit()
    return jsonify({'message': 'Schedule created successfully'}), 201

# 스케줄 조회
@app.route('/schedules', methods=['GET'])
def get_schedules():
    schedules = Schedule.query.all()
    return jsonify([{'id': sch.id, 'title': sch.title, 'description': sch.description, 'datetime': sch.datetime} for sch in schedules]), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 데이터베이스 테이블 생성
    app.run(debug=True)

