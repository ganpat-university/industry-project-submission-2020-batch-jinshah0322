class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                root_u, root_v = root_v, root_u
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]

            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_u] += 1

def difference_between_components(n, edges, queries):
    uf = UnionFind(n)
    components_sizes = []

    for u, v in edges:
        uf.union(u, v)

    for query in queries:
        components_sizes.append(uf.size[uf.find(query)] - uf.rank[uf.find(query)])

    return components_sizes


n = 6
edges = [(0, 1), (1, 2), (3, 4)]
queries = [0, 1, 2, 3, 4, 5]

result = difference_between_components(n, edges, queries)
print("Difference between sizes of smallest and largest components after each query:", result)
