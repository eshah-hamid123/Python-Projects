from datetime import datetime
from random import randint
import time


class Task:

    def progress(self):
        current_time = datetime.now()
        timeRN = current_time.strftime("%H:%M:%S")
        print(f'Task has started at time {timeRN}')
        r = randint(1, 15)
        # time.sleep(r * 1000)
        current_time = datetime.now()
        timeRN = current_time.strftime("%H:%M:%S")
        print(f'Server has done processing at {timeRN}')











