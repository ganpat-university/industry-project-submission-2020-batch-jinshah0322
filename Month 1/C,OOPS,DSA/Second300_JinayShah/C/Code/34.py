class HopcroftKarp:
    def __init__(self, graph):
        self.graph = graph
        self.match = {}
        self.dist = {}

    def bfs(self):
        queue = []
        for u in self.graph:
            if self.match.get(u) is None:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        self.dist[None] = float('inf')
        while queue:
            u = queue.pop(0)
            if u is None:
                continue
            for v in self.graph[u]:
                if self.dist[self.match.get(v)] == float('inf'):
                    self.dist[self.match.get(v)] = self.dist[u] + 1
                    queue.append(self.match.get(v))
        return self.dist[None] != float('inf')

    def dfs(self, u):
        if u is None:
            return True
        for v in self.graph[u]:
            if self.dist[self.match.get(v)] == self.dist[u] + 1 and self.dfs(self.match.get(v)):
                self.match[u] = v
                self.match[v] = u
                return True
        self.dist[u] = float('inf')
        return False

    def maximum_matching(self):
        matching = 0
        while self.bfs():
            for u in self.graph:
                if self.match.get(u) is None:
                    if self.dfs(u):
                        matching += 1
        return matching


graph = {'a': {1}, 'b': {1, 2}, 'c': {1, 2}, 'd': {2, 3, 4}, 'e': {3, 4}, 'f': {4, 5, 6}, 'g': {5, 6, 7}, 'h': {8}}

hk = HopcroftKarp(graph)
matching = hk.maximum_matching()

print("Maximum matching:", matching)
