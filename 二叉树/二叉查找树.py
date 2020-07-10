class TreeNode(object):
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def has_left(self):
        return self.left

    def has_right(self):
        return self.right

    def has_parent(self):
        return self.parent

    def is_left(self):
        return self.parent and self.parent.left == self

    def is_right(self):
        return self.parent and self.parent.right == self

    def is_leaf(self):
        return not (self.left or self.right)

    def is_root(self):
        return not self.parent

    def has_any_children(self):
        return self.right or self.left

    def has_both_children(self):
        return self.right and self.left

    def replace_node_data(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

        if self.has_left():
            self.left.parent = self
        if self.has_right():
            self.right.parent = self


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.length()

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, cur_node):
        # 比 当前的key 小 放到当前node 的左边
        if cur_node.key > key:
            if cur_node.has_left():
                self._put(key, value, cur_node.left)
            else:
                cur_node.left = TreeNode(key, value, parent=cur_node)
                return
        else:
            if cur_node.has_right():
                self._put(key, value, cur_node.right)
            else:
                cur_node.right = TreeNode(key, value, parent=cur_node)
                return

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        return self._get(key, self.root)

    def _get(self, key, cur_node):
        if not cur_node:
            return None
        if cur_node.key == key:
            return cur_node
        else:
            if cur_node.key > key:
                self._get(key, cur_node.left)
            else:
                self._get(key, cur_node.right)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, item):
        if self.get(item):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node = self.get(key)
            if node:
                self.remove(node)
                self.size -= 1
            else:
                raise KeyError('node not exits')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('node not exits')

    def remove(self, node):
        # 没有子节点
        if not node.has_any_children():
            if node.is_right():
                node.parent.right = None
            else:
                node.parent.left = None
        # 左右子节点 都存在
        elif node.has_both_children():
            succ = self.find_successor(node)
            self.splice_out(succ)
            node.key = succ.key
            node.value = succ.value
        # 只有一个子节点
        else:
            if node.has_left():
                if node.is_left():
                    node.parent.left = node.left
                    node.left.parent = node.parent
                elif node.is_right():
                    node.parent.right = node.left
                    node.left.parent = node.parent
                else:
                    node.replace_node_data(node.left.key, node.left.value, node.left.left, node.left.right)

            else:
                if node.is_left():
                    node.parent.left = node.right
                    node.right.parent = node.parent
                elif node.is_right():
                    node.parent.right = node.right
                    node.right.parent = node.parent
                else:
                    node.replace_node_data(node.right.key, node.right.value, node.right.left, node.right.right)

    def find_successor(self, node):
        succ = None
        if node.has_right():
            succ = self.find_min(node.right)
        else:
            if node.has_parent():
                if node.is_left():
                    succ = node.parent
                else:
                    node.parent.right = None
                    succ = self.find_successor(node.parent)
                    node.parent.right = node
        return succ

    @staticmethod
    def find_min(node):
        while node.has_left():
            node = node.left
        return node.left

    @staticmethod
    def splice_out(node):
        if node.is_leaf():
            if node.is_left():
                node.parent.left = None
            else:
                node.parent.right = None
        # 被选为后继节点的节点 只能存在右子节点 或者 左子节点
        elif node.has_any_children():
            if node.has_right():
                if node.is_left():
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.right.parent = node.parent
            else:
                if node.is_left:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
