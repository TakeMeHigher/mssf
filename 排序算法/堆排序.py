# -*- coding: utf-8 -*-
"""
Copyright (c) 2018,掌阅科技
All rights reserved.

摘    要: 堆排序.py
创 建 者: Chentaizhang
创建日期: 2019/2/13 15:03
"""


# 重新调整堆
def build(li, i, n):
    while True:
        max_index = i
        if 2 * i <= n and li[i] < li[2 * i]:
            max_index = 2 * i

        if 2 * i + 1 <= n and li[max_index] < li[2 * i + 1]:
            max_index = 2 * i + 1
        if max_index == i:
            break
        li[i], li[max_index] = li[max_index], li[i]
        i = max_index


# 创建堆
def create(li):
    """
    :param li:
    :return:
    """
    # 构建堆
    n = len(li) - 1
    # 对于完全二叉树来说 n/2+1 到 n 都是 叶子节点 我们不需要堆化(不需要参与比较)，因为叶子节点往下堆化只能跟自己做比较
    for i in range(n // 2, 0, -1):
        build(li, i, n)

    print(li)


# 删除最大元素
def remove_max(li):
    n = len(li) - 1
    if n < 1:
        return -1
    create(li)
    li[1] = li[n]
    build(li, 1, n - 1)


# 排序
def px(li):
    n = len(li) - 1
    if n < 1:
        return -1
    create(li)
    k = n
    while k > 1:
        li[1], li[k] = li[k], li[1]
        k -= 1
        build(li, 1, k)


# 向堆中插入一个 元素

def add(li, item):
    li.append(item)
    n = len(li) - 1
    i = n
    while i // 2 > 0 and li[i // 2] < li[i]:
        li[i // 2], li[i] = li[i // 2], li[i]
        i = i // 2


aa = [0, 7, 5, 19, 8, 4, 1, 20, 13, 16]
create(aa)
# remove_max(aa)
# px(aa)
add(aa, 12)
px(aa)
print(aa)
