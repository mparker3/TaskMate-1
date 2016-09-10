'''
Hieu Do
09/10/2016
'''

import datetime
import operator
from collections import deque

'''
Each task is a dictionary
  task_id              : integer
  name of the task     : string
  deadline             : datetime format
  length (in minutes)  : integer of range [5, 180]
  priority             : integer, 1=low, 2=medium, 3=high 
  slot_id              : integer
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

# to be used in ranktask(ALLTASK)
def _findTaskById(id):
  for i in ALLTASK:
    if i['task_id'] == id:
      return i
  return {}

# find the next available slot
def _findNextSlot():
  for i in TIMESLOTS:
    if i['task_id'] == 000:
      return i
  return {}

'''
Goal: assign ALL tasks (if possible) to a free slot
'''
def ranktask(ALLTASK):
  res = []

  # sort the queue by deadline: most -> least imminent 
  taskqueue =  deque(sorted(ALLTASK, key=operator.itemgetter('deadline')))

  # for i in taskqueue: print i
  # print taskqueue[0]

  visited = []

  while len(taskqueue) > 0:
    # print taskqueue
    slot = _findNextSlot()
    # assign the most immminent event to an available timeslot
    if slot != {}:
      if slot['length'] >= taskqueue[0]['length']:
        # assign task to slot
        slot['task_id'] = taskqueue[0]['task_id']
        taskqueue[0]['slot_id'] = slot['slot_id']
        taskqueue.popleft()
        # push to stack
        visited.append(slot)
      # go back to the most recent slot 
      else:
        while len(visited) > 0:
          # if the length of the task considering is longer than 
          # that of the occupying task,
          # replace
          if taskqueue[0]['length'] >= visited[-1]['length']:
            taskqueue.append(_findTaskById(visited[-1]['task_id']))
            visited[-1]['task_id'] = taskqueue[0]['task_id']
            taskqueue.popleft()
            visited.pop()

  for slot in TIMESLOTS: print slot


if __name__ == '__main__':
  ranktask(ALLTASK)
