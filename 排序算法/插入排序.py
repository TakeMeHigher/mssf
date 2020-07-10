# -*- coding: utf-8 -*-
"""
摘    要: 插入排序.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 14:38
"""


def func(li):
    """

    :param li:
    :return:
    """
    for i in range(1, len(li)):
        j = i - 1
        tmp = li[i]
        while j > 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp


aa = [1, 5, 2, 9, 6, 3, 4]
func(aa)
print(aa)
