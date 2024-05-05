from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, vertex, visited, stack):
        visited[vertex] = True

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        stack.append(vertex)

    def topological_sort(self):
        visited = [False] * self.vertices
        stack = []

        for vertex in range(self.vertices):
            if not visited[vertex]:
                self.topological_sort_util(vertex, visited, stack)

        return stack[::-1]  

g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

topological_order = g.topological_sort()
print("Topological Sorting Order:", topological_order)