class LinkNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LruLinkNodeList(object):
    def __init__(self, size):
        self.head = None
        self.size = 0
        self.data = set()
        self.size = size
        self.len = 0

    def view_page(self, data):
        if data in self.data:
            if self.head.data == data:
                return
            cur = self.head
            pre = None
            while cur:
                if cur.data == data:
                    pre.next = cur.next
                    cur.next = self.head
                    self.head = cur
                    return
                else:
                    pre = cur
                    cur = cur.next

        else:
            self.add(data)

    def add(self, data):
        new_node = LinkNode(data)
        self.data.add(data)
        if not self.head:
            self.head = new_node
            self.data.add(data)
            self.len += 1

        else:
            if self.len == self.size:
                cur = self.head
                pre = None
                while cur.next:
                    pre = cur
                    cur = cur.next
                self.data.remove(cur.data)
                pre.next = None
                self.len -= 1
            new_node.next = self.head
            self.head = new_node
            self.len += 1

    def create_link(self, data_list):
        """
        创建链表
        :param data_list: 数据列表
        :return:
        """
        self.len = len(data_list)
        self.head = LinkNode(data_list[0])
        self.data.add(data_list[0])
        cur = self.head
        for i in data_list[1:]:
            self.data.add(i)
            node = LinkNode(i)
            cur.next = node
            cur = node

    def print_link_node(self):
        """
        打印链表
        :return:
        """
        print(f"{self.data} === {self.len} === {self.size}")
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


if __name__ == '__main__':
    ll = [1,2,3,4]
    n_list = LruLinkNodeList(5)
    n_list.create_link(ll)
    n_list.view_page(5)
    n_list.print_link_node()
