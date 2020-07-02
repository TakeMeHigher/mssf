class Queue(object):

    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def push(self, data):
        self.stack_a.append(data)

    def pop(self):
        if len(self.stack_b) == 0:
            if len(self.stack_a) == 0:
                return
            for i in range(len(self.stack_a)):
                self.stack_b.append(self.stack_a.pop())

        return self.stack_b.pop()
