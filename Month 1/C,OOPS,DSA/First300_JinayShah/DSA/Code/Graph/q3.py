class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                print(current_vertex, end=' ')
                visited.add(current_vertex)
                for neighbor in self.graph.get(current_vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

my_graph = Graph()

my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(2, 5)
my_graph.add_edge(3, 6)

print("BFS starting from vertex 1:")
my_graph.bfs(1)