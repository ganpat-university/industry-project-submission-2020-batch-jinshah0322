from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, vertex, stack, visited):
        visited[vertex] = True

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, stack, visited)

        stack.append(vertex)

    def transpose(self):
        transposed_graph = Graph(self.vertices)

        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                transposed_graph.add_edge(neighbor, vertex)

        return transposed_graph

    def dfs_scc(self, vertex, scc, visited):
        visited[vertex] = True
        scc.append(vertex)

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_scc(neighbor, scc, visited)

    def find_scc(self):
        stack = []
        visited = [False] * self.vertices

        for vertex in range(self.vertices):
            if not visited[vertex]:
                self.dfs(vertex, stack, visited)

        transposed_graph = self.transpose()

        visited = [False] * self.vertices
        strongly_connected_components = []

        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                scc = []
                transposed_graph.dfs_scc(vertex, scc, visited)
                strongly_connected_components.append(scc)

        return strongly_connected_components

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

scc_result = g.find_scc()
print("Strongly Connected Components:", scc_result)