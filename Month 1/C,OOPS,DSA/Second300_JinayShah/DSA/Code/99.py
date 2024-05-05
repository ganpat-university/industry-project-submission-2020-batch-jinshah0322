from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited, circuit):
        visited[v] = True
        circuit.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, circuit)

    def is_connected(self):
        visited = [False] * self.vertices
        for i in range(self.vertices):
            if len(self.graph[i]) > 0:
                start = i
                break

        self.dfs(start, visited, [])

        for i in range(self.vertices):
            if not visited[i] and len(self.graph[i]) > 0:
                return False

        return True

    def eulerian_circuit(self):
        if not self.is_connected():
            return "Graph is not Eulerian"

        odd_count = 0
        for i in range(self.vertices):
            if len(self.graph[i]) % 2 != 0:
                odd_count += 1

        if odd_count > 2:
            return "Graph is not Eulerian"

        start = 0
        for i in range(self.vertices):
            if len(self.graph[i]) % 2 != 0:
                start = i
                break

        circuit = []
        self.dfs(start, [False] * self.vertices, circuit)

        return circuit


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

euler_circuit = g.eulerian_circuit()
print("Eulerian Circuit:", euler_circuit)