# -*- coding: utf-8 -*-
"""

摘    要: 堆排序.py
创 建 者: Chentaizhang
创建日期: 2020-07-10 18:10
"""


class Heap(object):
    def __init__(self):
        self.items = [0]
        self.count = 0

    def build_min_heap(self, index: int, end: int):
        """
        调整为 小根堆
        :param index: 开始数据的索引
        :param end: 结束的索引
        :return:
        """
        while True:
            min_index = index
            if index * 2 <= end and self.items[index] > self.items[index * 2]:
                min_index = index * 2
            if index * 2 + 1 <= end and self.items[min_index] > self.items[index * 2 + 1]:
                min_index = index * 2 + 1
            if min_index == index:
                break
            self.items[index], self.items[min_index] = self.items[min_index], self.items[index]
            index = min_index

    def build_max_heap(self, index: int, end: int):
        """
        调整为 大根堆
        :param index: 开始数据的索引
        :param end: 结束的索引
        :return:
        """
        while True:
            max_index = index
            if index * 2 <= end and self.items[index] < self.items[index * 2]:
                max_index = index * 2
            if index * 2 + 1 <= end and self.items[max_index] < self.items[index * 2 + 1]:
                max_index = index * 2 + 1
            if max_index == index:
                break
            self.items[index], self.items[max_index] = self.items[max_index], self.items[index]
            index = max_index

    def create_min_heap(self, data: list):
        """
        创建 小根堆
        :param data: 列表数据
        :return:
        """
        self.items.extend(data)
        self.count = len(data)
        for i in range(self.count // 2, 0, -1):
            self.build_min_heap(i, self.count)

    def create_max_heap(self, data: list):
        """
        创建 大根堆
        :param data: 列表数据
        :return:
        """
        self.items.extend(data)
        self.count = len(data)
        for i in range(self.count // 2, 0, -1):
            self.build_max_heap(i, self.count)

    def del_max(self):
        """
        删除最大元素
        :return:
        """
        self.items[1] = self.items.pop()
        self.count -= 1
        self.build_max_heap(1, self.count)

    def insert(self, data: int):
        """
        向堆中插入一个元素
        :param data:
        :return:
        """
        self.items.insert(1, data)
        self.count += 1
        self.build(1, self.count)

    def heap_sort_reverse(self):
        """
        堆排序 从大到小
        :return:
        """
        count = self.count
        while count > 1:
            self.items[1], self.items[count] = self.items[count], self.items[1]
            count -= 1
            self.build_min_heap(1, count)

    def heap_sort(self):
        """
        堆排序 从小到大
        :return:
        """
        count = self.count
        while count >= 1:
            self.items[1], self.items[count] = self.items[count], self.items[1]
            count -= 1
            self.build_max_heap(1, count)


aa = [7, 5, 19, 8, 4, 1, 20, 13, 16]
heap = Heap()
heap.create_min_heap(aa)
print(heap.items)
# print(heap.count)
# heap.del_max()
# print(heap.items)
# print(heap.count)
# heap.insert(15)
# heap.heap_sort()
# print(heap.items)

heap.heap_sort_reverse()
print(heap.items)
