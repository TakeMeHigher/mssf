# -*- coding: utf-8 -*-
"""
摘    要: 冒泡.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 13:54
"""


def mp(li):
    """

    :param li:
    :return:
    """
    for i in range(len(li)-1):
        change = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                change = True
        if not change:
            return


aa = [1, 5, 2, 9, 6, 3, 4]
mp(aa)
print(aa)
