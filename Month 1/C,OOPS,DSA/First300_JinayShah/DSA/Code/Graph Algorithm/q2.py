from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def articulation_points(self, u, visited, parent, disc, low, ap):
        children = 0
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                self.articulation_points(v, visited, parent, disc, low, ap)

                low[u] = min(low[u], low[v])

                if low[v] >= disc[u] and parent[u] != -1:
                    ap[u] = True

                if parent[u] == -1 and children > 1:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def find_articulation_points(self):
        visited = [False] * self.vertices
        disc = [-1] * self.vertices
        low = [-1] * self.vertices
        parent = [-1] * self.vertices
        ap = [False] * self.vertices

        for i in range(self.vertices):
            if not visited[i]:
                self.articulation_points(i, visited, parent, disc, low, ap)

        articulation_points_list = [i for i in range(self.vertices) if ap[i]]
        return articulation_points_list

# Example usage:
g = Graph(7)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(1, 6)
g.add_edge(3, 5)
g.add_edge(4, 5)

articulation_points_result = g.find_articulation_points()
print("Articulation Points:", articulation_points_result)