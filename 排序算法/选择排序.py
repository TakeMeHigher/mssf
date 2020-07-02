# -*- coding: utf-8 -*-
"""
Copyright (c) 2018,掌阅科技
All rights reserved.

摘    要: 选择排序.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 14:14
"""

def func(li):
    """
    :param li:
    :return:
    """
    for i in range(len(li)-1):
        mic = i
        for j in range(i+1, len(li)):
            if li[j] < li[mic]:
                mic = j
        if mic != i:
            li[i], li[mic] = li[mic], li[i]

aa = [1,5,2,9,6,3,4]
func(aa)
print(aa)