class Stack(object):

    def __init__(self):
        self.item = []

    def push(self, data):
        self.item.append(data)

    def pop(self):
        if not self.is_empty():
            return self.item.pop()

    def is_empty(self):
        return len(self.item) == 0

    def peek(self):
        if not self.is_empty():
            return self.item[len(self.item) - 1]

    def size(self):
        return len(self.item)
