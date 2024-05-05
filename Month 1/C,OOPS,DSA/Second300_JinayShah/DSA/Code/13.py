class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            if self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            elif self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            else:
                self.parent[rootU] = rootV
                self.rank[rootV] += 1

def dsu_on_trees(nodes, weights, edges):
    n = nodes
    dsu = DSU(n)

    for edge in edges:
        u, v = edge
        if dsu.find(u) != dsu.find(v):
            print(f"Union of nodes {u} and {v}")
            dsu.union(u, v)


nodes = 7
weights = [1, 2, 6, 4, 2, 0, 3]
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 6), (6, 7)]


dsu_on_trees(nodes, weights, edges)
