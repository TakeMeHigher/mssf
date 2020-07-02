# -*- coding: utf-8 -*-
"""
Copyright (c) 2018,掌阅科技
All rights reserved.

摘    要: 两个栈实现一个队列.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 18:01
"""
class Queue:
    def __init__(self):
        self.stockA = []
        self.stockB = []

    def push(self, node):
        self.stockA.append(node)

    def pop(self):
        if self.stockB == []:
            if self.stockA == []:
                return None
            else:
                for i in range(len(self.stockA)):
                    self.stockB.append(self.stockA.pop())
        return self.stockB.pop()