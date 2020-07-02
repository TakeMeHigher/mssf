class Stack(object):

    def __init__(self):
        self.queue_a = []
        self.queue_b = []

    def push(self, data):
        self.queue_a.append(data)

    def pop(self):
        if len(self.queue_b) == 0:
            if len(self.queue_a) == 0:
                return
            for i in range(len(self.queue_a)):
                self.queue_b.append(self.queue_a.pop(0))

        return self.queue_b.pop()



s = Stack()
s.push(1)
s.push(2)
s.push(3)


print(s.queue_a)
print(s.queue_b)

print(s.pop())
print(s.pop())