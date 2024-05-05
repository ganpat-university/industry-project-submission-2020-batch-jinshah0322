import heapq

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def add_vertex(self, value):
        self.vertices.add(value)
        self.edges[value] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.edges[vertex1].append((vertex2, weight))
        self.edges[vertex2].append((vertex1, weight))  

def prim(graph):
    start_vertex = next(iter(graph.vertices))  
    visited = set([start_vertex])
    minimum_spanning_tree = []
    priority_queue = [(weight, start_vertex, neighbor) for neighbor, weight in graph.edges[start_vertex]]
    heapq.heapify(priority_queue)

    while priority_queue:
        weight, current_vertex, neighbor = heapq.heappop(priority_queue)

        if neighbor not in visited:
            visited.add(neighbor)
            minimum_spanning_tree.append((current_vertex, neighbor, weight))

            for next_neighbor, next_weight in graph.edges[neighbor]:
                if next_neighbor not in visited:
                    heapq.heappush(priority_queue, (next_weight, neighbor, next_neighbor))

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

minimum_spanning_tree = prim(graph)

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")