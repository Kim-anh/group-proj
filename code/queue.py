import time


class Queue:
    def __init__(self, size):
        self.people = []
        self.size = size
        self.times = []
        self.last_time = None

    def insert(self, person):
        if len(self.people) < self.size:
            self.people.append(person)
            if self.last_time is None:
                self.last_time = int(time.time())
            if self.last_time is not None:
                self.times.append(int(time.time()) - self.last_time)
                self.last_time = int(time.time())
            print("inserted person into queue")
        else:
            print("Cannot insert person to queue, queue is full")
            return 1

    def leave(self):
        print(len(self.people))

    def __str__(self):
        return "People: " + ", ".join(self.people) + "\nTimes: " + ", ".join(str(x) for x in self.times)
