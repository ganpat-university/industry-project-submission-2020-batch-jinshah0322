from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.graph[v][u] = 0  # Add a reverse edge with initial capacity 0

    def bfs(self, source, sink, parent):
        visited = [False] * self.vertices
        queue = deque()
        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.popleft()

            for v, capacity in self.graph[u].items():
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[sink]

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.vertices
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

# Example usage:
g = Graph(6)
g.add_edge(0, 1, 16)
g.add_edge(0, 2, 13)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 12)
g.add_edge(2, 1, 4)
g.add_edge(2, 4, 14)
g.add_edge(3, 2, 9)
g.add_edge(3, 5, 20)
g.add_edge(4, 3, 7)
g.add_edge(4, 5, 4)

source = 0
sink = 5

max_flow = g.edmonds_karp(source, sink)
print("Maximum Flow in the Network:", max_flow)