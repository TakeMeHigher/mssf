# -*- coding: utf-8 -*-
"""
Copyright (c) 2018,掌阅科技
All rights reserved.

摘    要: 二分查找递归.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 14:09
"""


def func(li, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if li[mid] == target:
            return mid
        elif li[mid] < target:
            return func(li, mid + 1, high, target)
        elif li[mid] > target:
            return func(li, low, mid - 1, target)


aa = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = func(aa, 0, len(aa) - 1, 6)
print(index)

aa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(aa[-2:1:-2])
