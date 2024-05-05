class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def bellman_ford(self, source):
        distance = [float('inf')] * self.V
        distance[source] = 0

        for _ in range(self.V - 1):
            for u, v, weight in self.graph:
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

        for u, v, weight in self.graph:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                print("Graph contains negative weight cycle")
                return

        print("Vertex Distance from Source:")
        for i in range(self.V):
            print(f"{i} \t\t {distance[i]}")

g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

source_vertex = 0
g.bellman_ford(source_vertex)