# -*- coding: utf-8 -*-
"""
摘    要: 二分查找.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 14:00
"""


#
#
# def func(li, target):
#     """
#     :param li: list
#     :param target: 目标值
#     :return:
#     """
#     low = 0
#     high = len(li) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if li[mid] == target:
#             return mid
#         elif li[mid] < target:
#             low = mid + 1
#         elif li[mid] > target:
#             high = mid - 1
#         else:
#             print("{}不存在".format(target))
#
#
# aa = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# index = func(aa, 5)
# print(index)


def efcz(li, target):
    low = 0
    high = len(li) - 1
    while low < high:
        mid = (low + high) // 2
        if li[mid] == target:
            return mid
        elif li[mid] > target:
            high = mid - 1
        elif li[mid] < target:
            low = mid + 1
        else:
            print('no')


aa = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = efcz(aa, 5)
print(index)
