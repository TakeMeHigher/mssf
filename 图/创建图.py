class Graph(object):
    """
    无向图
    """

    def __init__(self, count: int):
        self.count = count  # 定点的个数
        self.linked_list = []  # 邻接表
        self.init_linked_list()
        self.found = False

    def init_linked_list(self):
        for i in range(self.count):
            self.linked_list[i] = []

    def add_bian(self, s: int, t: int):
        """
        无向图一条边添加 两次
        :param s:
        :param t:
        :return:
        """
        self.linked_list[s].append(t)
        self.linked_list[t].append(s)

    def bfs(self, start: int, target: int):
        """
        广度优先搜索
        :param start:
        :param target:
        :return:
        """
        # 用来存储已经被访问、但相连的顶点还没有被访问的顶点
        current_visit = [start]
        # visited 是用来记录已经被访问的顶点，用来避免顶点被重复访问。如果顶点 q 被访问，那相应的 visited[q]会被设置为 true。
        visited = [False] * self.count

        # prev 用来记录搜索路径。当我们从顶点 s 开始，广度优先搜索到顶点 t 后，prev 数组中存储的就是搜索的路径
        prev = [-1] * self.count

        while len(current_visit) > 0:
            res = current_visit.pop()
            for i in self.linked_list[res]:
                if not visited[i]:
                    prev[i] = res
                    visited[i] = True
                    if i == target:
                        self.print_road(prev, start, i)
                        return
                    current_visit.insert(0, i)

    def dfs(self, start: int, target: int):
        """
        深度优先搜索
        :param start:
        :param target:
        :return:
        """
        # visited 是用来记录已经被访问的顶点，用来避免顶点被重复访问。如果顶点 q 被访问，那相应的 visited[q]会被设置为 true。
        visited = [False] * self.count

        # prev 用来记录搜索路径。当我们从顶点 s 开始，广度优先搜索到顶点 t 后，prev 数组中存储的就是搜索的路径
        prev = [-1] * self.count

        self.dfs_util(start, target, visited, prev)
        self.print_road(prev, start, target)

    def dfs_util(self, start: int, target: int, visited: list, prev: list):
        """

        :param start:
        :param target:
        :param visited:
        :param prev:
        :return:
        """
        visited[start] = True
        if self.found:
            return
        if start == target:
            self.found = True
            return

        for res in self.linked_list[start]:
            if not visited[res]:
                prev[res] = start
                self.dfs_util(res, target, visited, prev)

    def print_road(self, prev: list, start: int, res: int):
        if prev[res] != -1 and start != res:
            print(prev, start, prev[res])
        print("res is {}", res)
