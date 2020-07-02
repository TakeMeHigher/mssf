# -*- coding: utf-8 -*-
"""
Copyright (c) 2018,掌阅科技
All rights reserved.

摘    要: 连续最大和.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 16:27
"""


def maxList(a):
    maxpre = realmax = a[0]
    length = len(a)
    for i in range(1, length):
        if realmax <= 0:
            realmax = a[i]
        else:
            realmax += a[i]
        if maxpre < realmax:
            maxpre = realmax
    return maxpre


sum1 = maxList([1, 2, 3, -1, -10, 5, 7, 8])
print(sum1)


def aa(a):
    max_pre, max_rel = a[0]

    for i in range(1, len(a)):
        if max_pre < 0:
            max_pre = a[i]
        else:
            max_pre += a[i]
        if max_rel < max_pre:
            max_rel = max_pre
    return max_rel
