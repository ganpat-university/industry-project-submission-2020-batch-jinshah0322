import heapq

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
        
    def add_vertex(self, value):
        self.vertices.add(value)
        self.edges[value] = []
        
    def add_edge(self, from_vertex, to_vertex, weight):
        self.edges[from_vertex].append((to_vertex, weight))
        self.edges[to_vertex].append((from_vertex, weight))  # For undirected graph

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start] = 0
    
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

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

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)

print(f"Shortest distances from vertex {start_vertex}:")
for vertex, distance in shortest_distances.items():
    print(f"To {vertex}: {distance}")
