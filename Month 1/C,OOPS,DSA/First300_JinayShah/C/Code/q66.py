class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = []

    def add_vertex(self, value):
        self.vertices.add(value)

    def add_edge(self, vertex1, vertex2, weight):
        self.edges.append((vertex1, vertex2, weight))

def kruskal(graph):
    def find(parent, vertex):
        if parent[vertex] == -1:
            return vertex
        return find(parent, parent[vertex])

    def union(parent, x, y):
        x_set = find(parent, x)
        y_set = find(parent, y)
        parent[x_set] = y_set

    graph.edges = sorted(graph.edges, key=lambda edge: edge[2])  # Sort edges by weight
    minimum_spanning_tree = []
    parent = {vertex: -1 for vertex in graph.vertices}

    for edge in graph.edges:
        vertex1, vertex2, weight = edge
        set1 = find(parent, vertex1)
        set2 = find(parent, vertex2)

        if set1 != set2:
            minimum_spanning_tree.append((vertex1, vertex2, weight))
            union(parent, set1, set2)

    return minimum_spanning_tree

graph = Graph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 10)
graph.add_edge('C', 'D', 3)
graph.add_edge('D', 'E', 7)
graph.add_edge('E', 'A', 8)
graph.add_edge('E', 'B', 6)

minimum_spanning_tree = kruskal(graph)

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")