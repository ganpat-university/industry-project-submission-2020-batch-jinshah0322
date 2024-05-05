class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def explore(self, vertex, visited, component):
        visited.add(vertex)
        component.append(vertex)
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                self.explore(neighbor, visited, component)

    def connected_components(self):
        visited = set()
        components = []

        for vertex in self.graph:
            if vertex not in visited:
                component = []
                self.explore(vertex, visited, component)
                components.append(component)

        return components

my_graph = Graph()

my_graph.add_edge(1, 2)
my_graph.add_edge(2, 3)
my_graph.add_edge(4, 5)

components = my_graph.connected_components()

print("Connected Components:")
for component in components:
    print(component)