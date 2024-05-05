class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

        return True


n = 10  
union_find = UnionFind(n)


union_find.union(0, 1)
union_find.union(2, 3)
union_find.union(4, 5)


print(union_find.find(0) == union_find.find(1))  
print(union_find.find(0) == union_find.find(4))  


union_find.union(1, 2)


print(union_find.find(0) == union_find.find(4))  
