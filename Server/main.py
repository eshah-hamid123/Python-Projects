from subject import Subject, Queue
from task import Task
import time
print('Queue Management System')

s = Subject()
tasks_served = 0
while True:
    time.sleep(2)
    task_generated = Task()
    s.new_task(task_generated)
    task_generated.progress()
    tasks_served += 1
    s.print_status(tasks_served)
    s.task_completed()

    choice = input('Print n if you want to close the queue system: ')
    if choice == 'n':
        break




