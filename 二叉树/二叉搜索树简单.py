class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def create_tree(li, start, end):
        if start > end:
            return
        mid = (start + end + 1) // 2
        node = Node(li[mid])
        node.left = Node.create_tree(li, start, mid - 1)
        node.right = Node.create_tree(li, mid + 1, end)
        return node


class Tree(object):
    def __init__(self):
        self.root = None

    def qxbl(self, root):
        """
        前序遍历
        :param root:
        :return:
        """
        if not root:
            return
        print(root.data)
        if root.left:
            self.qxbl(root.left)
        if root.right:
            self.qxbl(root.right)

    def search(self, data):
        node = self.root
        while node:
            if node.data == data:
                return node
            elif node.data > data:
                node = node.left
            else:
                node = node.right

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        p = self.root
        while p:
            if p.data > data:
                if not p.left:
                    p.left = Node(data)
                    return
                else:
                    p = p.left
            else:
                if not p.right:
                    p.right = Node(data)
                    return
                else:
                    p = p.right

    def delete(self, data):
        p = self.root
        if not p:
            return
        pp = None

        while p and p.data != data:
            pp = p
            if p.data > data:
                p = p.left
            else:
                p = p.right

        # 删除的是跟节点
        if not pp:
            self.root = None
            return

        # 存在两个字节点
        if p.left and p.right:
            Tree.delete_has_both_child_node(current=p)
        # 只有一个子节点
        elif p.left or p.left:
            Tree.have_one_child_node(p, pp)
        else:
            if pp.left == p:
                pp.left = None
            else:
                pp.right = None

    @staticmethod
    def delete_has_both_child_node(current):
        mc = current.right
        if not mc.left:
            current.data = mc.data
            current.right = mc.right
        else:
            mp = current
            while mc.left:
                mp = mc
                mc = mc.left

            current.data = mc.data
            mp.right = mc.left

    @staticmethod
    def have_one_child_node(current, parent):
        if current.left:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
        else:
            if parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right


ll = [1, 2, 3, 4, 5, 6, 6.1, 6.4, 7, 7.2, 8]
root = Node.create_tree(ll, 0, len(ll) - 1)
tree = Tree()
tree.root = root
tree.qxbl(root)
# ns = tree.search(5)
# print(ns.data)
#
# tree.insert(5.1)
# tree.qxbl(root)

print('-----------------')
tree.delete(3)
tree.qxbl(root)
