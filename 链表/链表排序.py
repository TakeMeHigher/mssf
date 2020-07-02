

class Node():
    def __init__(self, item=None):
        self.item = item
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None

    def create(self, item):
        self.head = Node(item[0])
        p = self.head
        for i in item[1:]:
            p.next = Node(i)
            p = p.next

    def print(self):
        p = self.head
        while p != None:
            print(p.item, end=' ')
            p = p.next
        print()

    def getItem(self, index):
        p = self.head
        count = 0
        while count != index:
            p = p.next
            count += 1
        return p.item

    def setItem(self, index, item):
        p = self.head
        count = 0
        while count < index :
            p = p.next
            count += 1
        p.item = item

    def swapItem(self, i, j):
        t = self.getItem(j)
        self.setItem(j, self.getItem(i))
        self.setItem(i, t)

    def quicksortofloop(self, left, right):
        tmp = self.getItem(left)
        while left < right:
            while left < right and self.getItem(right) > tmp:
                right -= 1

            self.swapItem(left, right)

            while left < right and self.getItem(left) < tmp:
                left += 1

            self.swapItem(left, right)
        self.setItem(left, tmp)

        return left

    def qk(self, left, right):
        if left < right:
            mid = self.quicksortofloop(left, right)
            self.qk(left, mid-1)
            self.qk(mid+1, right)


if __name__ == "__main__":
    L = LinkList()
    L.create([4, 2, 5, 3, 7, 9, 0, 1])
    L.print()
