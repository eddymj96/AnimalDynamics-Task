import numpy as np

class robot:
    position = np.array([0,0])
    def __init__(self, position):
        self.position = position
    def move(self, direction):
        self.position = self.position + direction


class queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        
    