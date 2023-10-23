class Queue:

    def __init__(self):
        self.size = 10
        self.queue = []
        for i in range(10):
            self.queue.append('NULL')
        self.front = self.rear = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.rear + 1) % self.size == self.front):
            print("The circular queue is full\n")

        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.front == -1):
            print("The circular queue is empty\n")
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False


class Subject:
    def __init__(self):
        self.TaskQueue = Queue()
        self.server = ['0', '0', '0']
        self.index = []

    def new_task(self, Specific_task):
        task_assigned = False
        if ((self.TaskQueue.rear + 1) % self.TaskQueue.size == self.TaskQueue.front):
            print('Queue is full')
        else:
            for i in range(3):
                if self.server[i] == '0':
                    self.server[i] = 'Busy'
                    self.index.append(i)
                    self.TaskQueue.enqueue(Specific_task)
                    print('Task enqueued')
                    break
            if not task_assigned:
                print('All servers are busy!')

    def task_completed(self):
        self.TaskQueue.dequeue()
        num = self.index.pop()
        self.server[num] = '0'


    def print_status(self, num):
        i = 1
        for s in self.server:

            if s == '0':
                print(f'Server {i}: Available')
            else:
                print(f'Server {i}: Busy, serving task {num}')
            i += 1

        awaiting_tasks = self.TaskQueue.rear - self.TaskQueue.front
        print(f'Queue has {awaiting_tasks} awaiting tasks')
        print(f'Total tasks served {num}' )
        t = num * 1000
        print(f'Total time {t} sec')











