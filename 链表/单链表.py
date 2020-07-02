class LinkNode(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkNodeList(object):
    def __init__(self):
        self.head = None

    def create_link(self, data_list):
        """
        创建链表
        :param data_list: 数据列表
        :return:
        """
        self.head = LinkNode(data_list[0])
        cur = self.head
        for i in data_list[1:]:
            node = LinkNode(i)
            cur.next = node
            cur = node

    def print_link_node(self):
        """
        打印链表
        :return:
        """
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


    def remove_last(self):
        cur = self.head
        pre = None
        while cur.next:
            pre = cur
            cur = cur.next

        pre.next = None

    def reverse(self):
        """
        反转链表 头插法
        :return:
        """
        cur = self.head.next
        self.head.next = None
        while cur:
            next = cur.next
            cur.next = self.head
            self.head = cur
            cur = next

    def find(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next

    def length(self):
        """
        链表的长度
        :return:
        """
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def qu_chong(self):
        """
        去重
        :return:
        """
        cur = self.head
        li = []
        pre = None
        while cur:
            if cur.data not in li:
                li.append(cur.data)
                pre = cur
                cur = cur.next
            else:
                pre.next = cur.next
                pre = pre
                cur = cur.next

    def add(self, data):
        """
        头部添加
        :return:
        """
        new_node = LinkNode(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        """
        从尾部添加
        :param data:
        :return:
        """
        cur = self.head
        while cur.next:
            cur = cur.next
        new_node = LinkNode(data)
        cur.next = new_node

    def get_data(self, index):
        """
        获取链表指定索引的值
        :param index:
        :return:
        """
        cur = self.head
        count = 0
        while cur:
            if count == index:
                return cur.data
            cur = cur.next
            count += 1

    def set_data(self, index, data):
        """
        给对应的index 设置值
        :param index:
        :param data:
        :return:
        """
        cur = self.head
        count = 0
        while cur:
            if count == index:
                cur.data = data
                return
            cur = cur.next
            count += 1

    def swap_data(self, index1, index2):
        """
        交换两个索引对应的值
        :param index1:
        :param index2:
        :return:
        """
        index1_data = self.get_data(index1)
        self.set_data(index1, self.get_data(index2))
        self.set_data(index2, index1_data)

    def sort(self, left, right):
        """
        链表排序
        :return:
        """
        if left < right:
            mid = self.qk_sort(left, right)
            self.sort(left, mid)
            self.sort(mid + 1, right)

    def qk_sort(self, left, right):
        """
         快排实现
        :param left:
        :param right:
        :return:
        """
        tem = self.get_data(left)
        while left < right:
            while left < right and self.get_data(right) >= tem:
                right -= 1
            self.swap_data(left, right)

            while left < right and self.get_data(left) <= tem:
                left += 1

            self.swap_data(left, right)
        self.set_data(left, tem)
        return left

    def xl_reverse(self):
        """
        相邻元素 反转
        :return:
        """
        cur = self.head
        count = 0
        while cur:
            next = cur.next
            if next:
                self.swap_data(count, count + 1)
                if next.next:
                    count = count + 2
                    cur = next.next
                else:
                    return
            else:
                return

    def k_reverse(self, k):
        """
                相邻的k个元素 反转
                K链表翻转是指把每K个相邻的结点看成一组进行翻转，如果剩余结点不足K个，则保持不变。
                假设给定链表1-＞2-＞3-＞4-＞5-＞6-＞7和一个数K，如果K的值为2，那么翻转后的链表为2-＞1-＞4-＞3-＞6-＞5-＞7。如果K的值为3，那么翻转后的链表为：3-＞2-＞1-＞6-＞5-＞4-＞7。
                :param k:
                :return:
                """
        n = int(self.length() / k)
        dic = {}
        for i in range(1, n + 1):
            dic[i] = LinkNodeList()
        last_len = 0
        for i in range(1, n + 1):
            cur = dic[i].head
            for j in range(last_len, i * k):
                data = self.get_data(j)
                if data:
                    cur.next = LinkNode(data)
                    cur = cur.next

            last_len = i * k
            dic[i].reverse()

        new_list = LinkNodeList()
        cur = new_list.head
        for i in range(1, n + 1):
            cur.next = dic[i].head.next
            cur = dic[i].get_node(k - 1)

        cur.next = self.get_node(k * n)
        new_list.print_link_node()






if __name__ == '__main__':
    ll = [1, 3, 2,1, 8, 4, 9, 11, 76]
    n_list = LinkNodeList()
    n_list.create_link(ll)

    n_list.remove_last()

    n_list.print_link_node()

    # print(n_list.find(4).data)

    # n_list.reverse()
    # print(n_list.length())
    # n_list.qu_chong()

    # n_list.add(11)
    # n_list.append(66)
    # n_list.print_link_node()
    # print(n_list.get_data(3))



    # n_list.sort(0, n_list.length()-1)
    # n_list.xl_reverse()
    # n_list.k_reverse(3)
    # n_list.print_link_node()
    # n_list.length()
"""
姓名: 三和大神
工作经验:两年
擅长方向：
python java 前端开发 个人比较喜欢研究中间件相关知识 如 docker redis nginx rabbitmq kafka mysql k8s celery等

工作经历1： 北京**科技有限公司
负责公司的web开发, 前后端服务都写，后端为python,前端为vue, 在这期间把我们组的服务全部实现容器化 用docker，
docker，mysql，rabbitmq， celery接触的比较多

工作经历2: 北京**证券公司
服务web服务，以及量化相关需求，这期间逐渐接触金融知识，主要用
python和Java提供服务，python负责数据的清洗以及分析，Java提供web服务
redis mongodb, mysql 用的比较多 其他较少
"""
