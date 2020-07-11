# -*- coding: utf-8 -*-
"""
摘    要: 归并排序.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 16:15
"""


def func(li, low, mid, high):
    """
    :param li:
    :param low:
    :param mid:
    :param high:
    :return:
    """
    i = low
    j = mid + 1
    ll = []

    while i <= mid and j <= high:
        if li[i] <= li[j]:
            ll.append(li[i])
            i += 1
        else:
            ll.append(li[j])
            j += 1
    while i <= mid:
        ll.append(li[i])
        i += 1
    while j <= high:
        ll.append(li[j])
        j += 1
    li[low:high + 1] = ll


def _merge_sort(li, low, high):
    if low < high:  # 至少两个元素
        mid = (low + high) // 2
        _merge_sort(li, low, mid)
        _merge_sort(li, mid + 1, high)
        func(li, low, mid, high)
        print(li[low:high + 1])


def _merge_sort1(li, low, high):
    if low < high:
        mid = (low + high) // 2
        _merge_sort1(li, low, mid)
        _merge_sort1(li, mid + 1, high)


def merge_sort(li, mid, low, high):
    i = low
    j = mid + 1
    ll = l


