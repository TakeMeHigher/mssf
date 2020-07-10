# -*- coding: utf-8 -*-
"""
摘    要: 堆排序(heap).py
创 建 者: Chentaizhang
创建日期: 2019/2/13 15:56
"""

import heapq
import random

li = [5, 8, 7, 6, 1, 4, 9, 3, 2]

heapq.heapify(li)
print(li)
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))


def heap_sort(li):
    heapq.heapify(li)
    n = len(li)
    new_li = []
    for i in range(n):
        new_li.append(heapq.heappop(li))
    return new_li


li = list(range(10000))
random.shuffle(li)
li = heap_sort(li)
print(li)

# print(heapq.nlargest(100, li))

# heapq.heapify()
