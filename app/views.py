from app import app
from flask import jsonify, \
                  abort, \
                  render_template, \
                  send_from_directory, \ 
                  url_for, request

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/tasks/', methods=['GET'])
def get_all_tasks():
  return jsonify(tasks)

@app.route('/tasks/<int:date>', methods=['GET'])
def get_sorted_tasks(date):
  tasks = ['task A', 'task B', 'task C']
  return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_new_task():
  if not request.json or not 'name' in request.json:
    abort(400)
  return 