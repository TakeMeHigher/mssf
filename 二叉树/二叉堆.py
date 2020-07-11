"""

摘    要: 堆排序.py
创 建 者: Chentaizhang
创建日期: 2020-07-10 18:10
"""


class Heap(object):
    def __init__(self):
        self.size = 0
        self.heap_list = [0]

    def build_heap(self, data):
        i = len(data) // 2
        self.size = len(data)
        self.heap_list = [0] + data
        while i > 0:
            self.pre_down(i)
            i -= 1

    def pre_down(self, i):
        while i * 2 <= self.size:
            m = self.get_min_child(i)
            if self.heap_list[i] > self.heap_list[m]:
                item = self.heap_list[i]
                self.heap_list[i] = self.heap_list[m]
                self.heap_list[m] = item
            i = m

    def get_min_child(self, i):
        if i * 2 + 1 > self.size:
            return 2 * i
        else:
            if self.heap_list[2 * i + 1] > self.heap_list[2 * i]:
                return 2 * i
            else:
                return 2 * i + 1

    def del_min(self):
        res = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size = self.size - 1
        self.heap_list.pop()
        self.pre_down(1)
        return res

    def insert_data(self, data):
        self.heap_list.append(data)
        self.size += 1
        self.per_up(self.size)

    def per_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                item = self.heap_list[i]
                self.heap_list[i] = self.heap_list[i // 2]
                self.heap_list[i // 2] = item
            i = 1 // 2


if __name__ == '__main__':
    heap = Heap()
    ll = [1, 3, 5, 4, 2]
    heap.build_heap(ll)
    print(heap.size)
    print(heap.heap_list)
    #
    # while heap.size > 0:
    #     print(heap.del_min())

    heap.insert_data(6)
    print(heap.heap_list)
