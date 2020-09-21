from collections import deque


class ErTree(object):
    def __init__(self):
        self.lchild = None
        self.rchild = None
        self.max_sum = 0

    def zxbl(self, root):
        """
        中序遍历
        :param root:
        :return:
        """
        if not root:
            return
        if root.lchild:
            self.zxbl(root.lchild)
        print(root.data)

        if root.rchild:
            self.zxbl(root.rchild)

    def qxbl(self, root):
        """
        前序遍历
        :param root:
        :return:
        """
        if not root:
            return
        print(root.data)
        if root.lchild:
            self.qxbl(root.lchild)
        if root.rchild:
            self.qxbl(root.rchild)

    def hxbl(self, root):
        """
        后序遍历
        :param root:
        :return:
        """
        if not root:
            return
        if root.lchild:
            self.qxbl(root.lchild)
        if root.rchild:
            self.qxbl(root.rchild)
        print(root.data)

    def cxpl(self, root):
        """
        层序遍历
        :param root:
        :return:
        """
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            print(node.data)
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    def change_array_to_tree(self, li, start, end):
        """
         如何把一个有序整数数组放到二叉树中
        :param li:
        :param start:
        :param end:
        :return:
        """
        if start > end:
            return None
        mid = (start + end + 1) // 2

        root = ErTree()
        root.data = li[mid]
        root.lchild = self.change_array_to_tree(li, start, mid - 1)
        root.rchild = self.change_array_to_tree(li, mid + 1, end)
        return root

    def max_sum_child_tree(self, root, max_node):
        """
        如何求一棵二叉树的最大子树和
        :return:
        """
        if not root:
            return 0
        lnum = self.max_sum_child_tree(root.lchild, max_node)
        rnum = self.max_sum_child_tree(root.rchild, max_node)

        a_sum = root.data + lnum + rnum

        if a_sum > self.max_sum:
            self.max_sum = a_sum
            max_node.data = a_sum

        return a_sum


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6, 7]
    tree = ErTree()
    root = tree.change_array_to_tree(li, 0, len(li) - 1)
    # tree.zxbl(root)
    # tree.qxbl(root)
    tree.hxbl(root)
