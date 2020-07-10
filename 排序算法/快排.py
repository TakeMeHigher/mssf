# -*- coding: utf-8 -*-
"""
摘    要: 快排.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 14:46
"""


def func(li, left, right):
    """
    :param li:
    :param left:
    :param right:
    :return:
    """
    tmp = li[left]
    while left < right:
        while left < right and li[right] <= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] >= tmp:
            left += 1
        li[right] = li[left]

    li[left] = tmp
    return left


def px(li, left, right):
    """
    :param li:
    :param left:
    :param right:
    :return:
    """
    if left <= right:
        mid = func(li, left, right)
        px(li, mid + 1, right)
        px(li, left, mid - 1)


def top_k(li, low, high, k):
    if low < high:
        mid = func(li, low, high)
        print(f'{mid}')
        if mid == k - 1:
            print(mid)
            print(li[mid])
            return mid
        elif mid < k - 1:
            top_k(li, mid + 1, high, k)
        elif mid > k - 1:
            top_k(li, low, mid, k)



aa = [1, 5, 2, 9, 6,4,3, 4]
px(aa, 0, len(aa) - 1)
print(aa)

top_k(aa, 0, len(aa)-1, 8)
