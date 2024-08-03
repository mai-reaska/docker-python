from flask import Flask #type:ignore
from flask import make_response #type:ignore
from flask import jsonify,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:dbApi2024!@localhost:5432/api_db"

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = "task"
    id = Column(Integer(), primary_key=True,autoincrement=True)
    title = Column(String(20), nullable=False)

with app.app_context():
    db.create_all()

     
@app.route("/")
def hello_world():
    return "testing api aa"

@app.route('/task', methods=('GET', 'POST'))
def task_input():
    task = Task.query.all()
    task_list = [
        {'id': tasks.id,'title': tasks.title} for tasks in task
    ]
    return jsonify({"Task":task_list})

@app.route('/addtask', methods=["POST"])
def creat_task():
    data = request.get_json()
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'smg':'task add too'},2001)
    
if __name__ == '__main__':
    app.run(debug=True)