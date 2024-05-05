from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited.add(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                if self.is_cyclic_util(neighbor, visited, v):
                    return True
            elif parent != neighbor:
                return True

        return False

    def is_cyclic(self):
        visited = set()
        print(self.graph)
        for vertex in self.graph:
            if vertex not in visited:
                if self.is_cyclic_util(vertex, visited, None):
                    return True

        return False


my_graph = Graph()

my_graph.add_edge(0, 1)
my_graph.add_edge(1, 2)
my_graph.add_edge(2, 0)
my_graph.add_edge(1, 3)

if my_graph.is_cyclic():
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")
