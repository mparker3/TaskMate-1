from app import app
from flask import jsonify, abort

@app.route('/')
def index():
  return "Task.me landing page"

@app.route('/tasks', methods=['GET'])
def get_sorted_tasks():
  tasks = ['task A', 'task B', 'task C']
  return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_new_task():
  return 