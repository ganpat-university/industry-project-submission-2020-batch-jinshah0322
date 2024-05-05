class WeightedUnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def weighted_union_find_example():
    n = 10
    uf = WeightedUnionFind(n)

    
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(6, 7)
    uf.union(8, 9)
    uf.union(1, 9)

    
    print("Root of 1:", uf.find(1))
    print("Root of 3:", uf.find(3))
    print("Root of 5:", uf.find(5))
    print("Root of 7:", uf.find(7))
    print("Root of 9:", uf.find(9))

weighted_union_find_example()
