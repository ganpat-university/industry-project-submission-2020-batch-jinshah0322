class EulerTourTree:
    def __init__(self, n):
        self.n = n
        self.tree = [[] for _ in range(n)]
        self.euler_tour = []
        self.first_occurrence = [-1] * n
        self.depths = []
        self.construct_euler_tour()

    def add_edge(self, u, v):
        self.tree[u].append(v)
        self.tree[v].append(u)
        self.construct_euler_tour()

    def construct_euler_tour(self):
        self.euler_tour = []
        self.first_occurrence = [-1] * self.n
        self.depths = []
        self.dfs(0, 0)
        self.construct_segment_tree()

    def dfs(self, u, depth):
        if self.first_occurrence[u] == -1:
            self.first_occurrence[u] = len(self.euler_tour)
        self.euler_tour.append(u)
        self.depths.append(depth)

        for v in self.tree[u]:
            if self.first_occurrence[v] == -1:
                self.dfs(v, depth + 1)
                self.euler_tour.append(u)
                self.depths.append(depth)

    def construct_segment_tree(self):
        self.segment_tree = [0] * (2 * len(self.euler_tour))
        for i, depth in enumerate(self.depths):
            self.segment_tree[len(self.euler_tour) + i] = depth

        for i in range(len(self.euler_tour) - 1, 0, -1):
            self.segment_tree[i] = min(self.segment_tree[2 * i], self.segment_tree[2 * i + 1])

    def query_lca(self, u, v):
        l, r = self.first_occurrence[u], self.first_occurrence[v]
        if l > r:
            l, r = r, l
        r += 1

        result = float('inf')
        while l < r:
            if l % 2 == 1:
                result = min(result, self.segment_tree[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                result = min(result, self.segment_tree[r])
            l //= 2
            r //= 2

        return result


n = 6
ett = EulerTourTree(n)

ett.add_edge(0, 1)
ett.add_edge(1, 2)
ett.add_edge(1, 3)
ett.add_edge(2, 4)
ett.add_edge(2, 5)


lca = ett.query_lca(4, 5)
print("Lowest Common Ancestor of 4 and 5:", lca)  
