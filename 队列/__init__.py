"""
实现一个队列的数据结构，使其具有入队列、出队列、查看队列首尾元素、查看队列大小等功能。
"""


class Queue(object):

    def __init__(self):
        self.item = []

    def enqueue(self, data):
        self.item.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.item.pop(0)

    def is_empty(self):
        return len(self.item) == 0

    def size(self):
        return len(self.item)
