class PersistentUnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  
        self.time = [float('inf')] * n  

    def find(self, x, t):
        if self.time[x] > t:
            return x
        return self.find(self.parent[x], t)

    def union(self, x, y, t):
        root_x = self.find(x, t)
        root_y = self.find(y, t)

        if root_x != root_y:
            
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1

    def connected(self, x, y, t):
        return self.find(x, t) == self.find(y, t)

class DynamicConnectivity:
    def __init__(self, n):
        self.uf = PersistentUnionFind(n)
        self.time = 0  

    def add_edge(self, x, y):
        self.uf.union(x, y, self.time)
        self.time += 1

    def remove_edge(self, x, y):
        
        self.uf = PersistentUnionFind(len(self.uf.parent))
        self.time = 0  
        for t in range(self.time):
            if t != self.time - 1:
                for i in range(len(self.uf.parent)):
                    self.uf.parent[i] = self.uf.find(i, t)

    def query(self, x, y, t):
        return self.uf.connected(x, y, t)


n = 5  
dc = DynamicConnectivity(n)


dc.add_edge(0, 1)
dc.add_edge(1, 2)
dc.add_edge(2, 3)


print(dc.query(0, 3, dc.time - 1))  


dc.remove_edge(1, 2)


print(dc.query(0, 3, dc.time - 1))  
