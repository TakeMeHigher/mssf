from collections import deque


class Lru(object):
    """
    LRU 缓存 实现
    """
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.set = set()

    def enqueue(self, data):
        if len(self.queue) == self.size:
            pop_data = self.queue.pop()
            self.set.remove(pop_data)

        self.queue.appendleft(data)
        self.set.add(data)

    def view_page(self, data):
        if data in self.set:
            self.queue.remove(data)
            self.queue.appendleft(data)
        else:
            self.enqueue(data)

    def print_queue(self):
        while len(self.queue) > 0:
            print(self.queue.popleft())




if __name__ == '__main__':
    lru = Lru(3)
    lru.enqueue(1)
    lru.enqueue(2)
    lru.enqueue(3)
    lru.view_page(2)
    lru.view_page(3)
    lru.enqueue(4)
    lru.print_queue()
