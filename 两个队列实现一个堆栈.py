# -*- coding: utf-8 -*-
"""
摘    要: 实现一个堆栈.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 16:58
"""


class Stock:
    def __init__(self):
        self.queueA = []
        self.queueB = []

    def push(self, node):
        self.queueA.append(node)

    def pop(self):
        if len(self.queueA) == 0:
            return None
        while len(self.queueA) != 1:
            self.queueB.append(self.queueA.pop(0))
        print(self.queueA, '---')
        print(self.queueB)
        self.queueA, self.queueB = self.queueB, self.queueA  # 交换是为了下一次的pop
        return self.queueB.pop()


s = Stock()

s.push(1)
s.push(2)
s.push(3)

print(s.queueA)
print(s.queueB)

print(s.pop())
