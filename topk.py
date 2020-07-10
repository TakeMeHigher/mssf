# -*- coding: utf-8 -*-
"""
摘    要: topk.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 15:33
"""


def func(li, low, high):
    """

    :param li:
    :param low:
    :param high:
    :return:
    """
    i = low
    j = 2*i+1
    tmp = li[low]

    while j <= high:
        if j+1 <= high and li[j+1] < li[j]:
            j += 1
        if tmp > li[j]:
            li[i] = li[j]
            i = j
            j = i*2 +1
        else:
            break
    li[i] = tmp


def topk(li, k):
    """
    :param li:
    :param k:
    :return:
    """
    l_k = li[:k]
    for i in range(k//2 -1, -1, -1):
        func(l_k, i , k-1)

    for i in range(k, len(li)):
        if li[i] > l_k[0]:
            l_k[0] = li[i]
            func(l_k,0, k-1)
    print(l_k)

    # 下面这一步 可以要 也可以不要 排序用
    for i in range(k-1, -1, -1):
        l_k[0], l_k[i] = l_k[i], l_k[0]
        func(l_k,0, i-1)
    return l_k


l = [1,9,62,90,80,6,4,45,5,32]
l_k = topk(l,5)
print(l_k)



