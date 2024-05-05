class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start):
        # Initializ distances with infinity for all vertices
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0

        # Set to keep track of processed vertices
        processed = set()

        while len(processed) < len(self.graph):
            # Find the minimum distance vertex not yet processed
            unprocessed_vertices = []
            for v in distances.keys():
                if v not in processed:
                    unprocessed_vertices.append(v)

            min_distance_vertex = min(unprocessed_vertices, key=distances.get)
            current_vertex = min_distance_vertex

            # Mark the current vertex as processed0
            processed.add(current_vertex)

            # Update distances for neighboring vertices
            for neighbor, weight in self.graph.get(current_vertex, []):
                distance = distances[current_vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances

my_graph = Graph()

my_graph.add_edge('A', 'B', 4)
my_graph.add_edge('A', 'C', 2)
my_graph.add_edge('B', 'C', 5)
my_graph.add_edge('B', 'D', 10)
my_graph.add_edge('C', 'D', 3)
my_graph.add_edge('D', 'A', 7)

shortest_paths = my_graph.dijkstra('A')

for vertex, distance in shortest_paths.items():
    print(f"Shortest distance from A to {vertex}: {distance}")