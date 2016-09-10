from app import app
from taskranker import *
from flask import jsonify, \
                  abort, \
                  render_template, \
                  send_from_directory, \
                  url_for, \
                  request

'''
Initialize some global variables for testing purpose
ALLTASKS: arrays of tasks to be completed
TIMESLOTS: arrays of available timeslots in the user's schedule
'''
# (datetime.datetime.now() + datetime.timedelta(days=7)).strftime('%Y-%m-%d %H:%M')
# sample tasks
task1 = {'task_id'  : 001, 
        'name'     : 'Call mom', 
        'deadline' : datetime.datetime(2016, 9, 12, 22, 30).strftime('%Y-%m-%d %H:%M'), 
        'length'   : 10, 
        'priority' : 1, 
        'slot_id'  : 000
        }
task2 = {'task_id'  : 002, 
        'name'     : 'Do CS homework', 
        'deadline' : datetime.datetime(2016, 9, 18, 17, 00).strftime('%Y-%m-%d %H:%M'), 
        'length'   : 120, 
        'priority' : 3, 
        'slot_id'  : 000
        }
task3 = {'task_id'  : 003, 
        'name'     : 'Eat', 
        'deadline' : datetime.datetime(2016, 9, 14, 11, 15).strftime('%Y-%m-%d %H:%M'), 
        'length'   : 60, 
        'priority' : 3, 
        'slot_id'  : 000
        }
# storing all tasks needed to complete
ALLTASK = [task1, task2, task3]

'''
Each timelot is a dictionary
  slot_id              : integer
  starttime            : datetime.time format
  length (in minutes)  : integer of range [5, 180]
  task_id              : integer
'''
slot1 = {'slot_id'  : 001, 
        'startime'  : datetime.datetime(2016, 9, 12, 22, 30).strftime('%Y-%m-%d %H:%M'), 
        'length'    : 60, 
        'task_id'   : 000
        } 
slot2 = {'slot_id'  : 002, 
        'startime'  : datetime.datetime(2016, 9, 13, 17, 00).strftime('%Y-%m-%d %H:%M'), 
        'length'    : 120, 
        'task_id'   : 000
        } 
slot3 = {'slot_id'  : 003, 
        'startime'  : datetime.datetime(2016, 9, 14, 8, 00).strftime('%Y-%m-%d %H:%M'), 
        'length'    : 30, 
        'task_id'   : 000
        }                 
slot4 = {'slot_id'  : 004, 
        'startime'  : datetime.datetime(2016, 9, 14, 13, 30).strftime('%Y-%m-%d %H:%M'), 
        'length'    : 60, 
        'task_id'   : 000
        }
slot5 = {'slot_id'  : 005, 
        'startime'  : datetime.datetime(2016, 9, 14, 23, 00).strftime('%Y-%m-%d %H:%M'), 
        'length'    : 10, 
        'task_id'   : 000
        }  
# storing free time slots      
TIMESLOTS = [slot1, slot2, slot3, slot4, slot5]

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/tasks/', methods=['GET'])
def get_all_tasks():
  # the returned value of ranktask function
  timeSlotsUsed = ranktask(ALLTASK, TIMESLOTS)
  tasks = []

  for slot in timeSlotsUsed:
    if slot['task_id'] != 0:
      temp = {}
      temp['time_slot'] = slot
      temp['task'] = findTaskDetailsById(slot['task_id'], ALLTASK)
      tasks.append(temp)

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