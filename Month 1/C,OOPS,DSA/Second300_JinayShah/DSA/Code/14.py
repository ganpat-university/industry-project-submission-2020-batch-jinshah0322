class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

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


n = 6
uf = UnionFind(n)


uf.union(0, 1)
uf.union(1, 2)
uf.union(2, 3)


print(uf.find(0))  
print(uf.find(3))  
