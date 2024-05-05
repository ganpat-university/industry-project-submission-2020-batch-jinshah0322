class PersistentUnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.time_stamp = [0] * size  

    def find(self, x, time):
        if self.time_stamp[x] > time:
            return x  
        if self.parent[x] == x:
            return x
        root_at_time = self.find(self.parent[x], time)
        self.time_stamp[x] = time  
        return root_at_time

    def union(self, x, y, time):
        root_x = self.find(x, time)
        root_y = self.find(y, time)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

    def query(self, x, time):
        return self.find(x, time)


size = 6
persistent_union_find = PersistentUnionFind(size)


persistent_union_find.union(0, 1, 1)
persistent_union_find.union(1, 2, 1)
persistent_union_find.union(3, 4, 1)


persistent_union_find.union(4, 5, 2)


result_at_time_1 = persistent_union_find.query(2, 1)
print("Element 2 at Time 1:", result_at_time_1)  


result_at_time_2 = persistent_union_find.query(2, 2)
print("Element 2 at Time 2:", result_at_time_2)  
