class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, next_):
        self.next = next_


class LinkedList(object):
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
            print(p.value, end=' ')
            p = p.next
        print()


    def is_empty(self):
        """检测是否为空"""
        return self.head == None


    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count


    def add(self, value):
        """在链表的最前端添加元素"""
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node


    def append(self, value):
        """在链表的最后端添加元素"""
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()
            current.set_next(new_node)


    def search(self, value):
        """查找某个元素是否在链表中"""
        current = self.head
        is_exit = False
        while current and not is_exit:
            if current.get_value() == value:
                is_exit = True
            else:
                current = current.get_next()
        return is_exit


    def index(self, value):
        """查看某个元素在链表中的索引"""
        current = self.head
        count = 0
        is_exit = False
        while current and not is_exit:
            count += 1
            if current.get_value() == value:
                is_exit = True
            else:
                current = current.get_next()

        if is_exit:
            return count
        else:
            print('{}在链表中不存在'.format(value))


    def remove(self, value):
        """删除链表中的某项元素"""
        current = self.head
        pre = None
        while current:
            if current.get_value() == value:
                if pre:
                    pre.set_next(current.get_next())
                else:
                    self.head = current.get_next()
            else:
                pre = current
                current = current.get_next()


    def insert(self, pos, value):
        """在列表的指定位置插入一个节点"""
        if pos < 1:
            self.add(value)
        elif pos >= self.length():
            self.append(value)
        else:
            count = 1
            pre = None
            current = self.head
            new_node = Node(value)
            while count < pos:
                count += 1
                pre = current
                current = current.get_next()

            pre.set_next(new_node)
            new_node.set_next(current)

    def reverse(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            if not temp:
                break
            pre = head
            head = temp
        return head

    def reverse1(self):
        cur = self.head.next
        next = cur.next









if __name__ == '__main__':
    L = LinkedList()
    L.create([4, 2, 5, 3, 7, 9, 0, 1])
    head = L.reverse(L.head)
    L.head = head
    print(L.head.value)
    L.print()
