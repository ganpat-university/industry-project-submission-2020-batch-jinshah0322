from collections import defaultdict
from queue import Queue

class FlowNetwork:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.graph[v][u] = 0  

    def ford_fulkerson(self, source, sink):
        parent = {}

        max_flow = 0
        while True:
            residual_graph, path_capacity = self.bfs(source, sink, parent)
            if path_capacity == 0:
                break

            max_flow += path_capacity

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_capacity
                self.graph[v][u] += path_capacity
                v = u

        min_cut = self.find_min_cut(source, parent)
        return max_flow, min_cut

    def bfs(self, source, sink, parent):
        visited = set()
        queue = Queue()
        queue.put(source)
        visited.add(source)
        parent[source] = None

        while not queue.empty():
            u = queue.get()

            for v, capacity in self.graph[u].items():
                if v not in visited and capacity > 0:
                    queue.put(v)
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        # Found a path
                        path_capacity = self.find_path_capacity(source, sink, parent)
                        return self.graph, path_capacity

        return None, 0

    def find_path_capacity(self, source, sink, parent):
        v = sink
        path_capacity = float('inf')
        while parent[v] is not None:
            u = parent[v]
            path_capacity = min(path_capacity, self.graph[u][v])
            v = u
        return path_capacity

    def find_min_cut(self, source, parent):
        min_cut = set()
        for u in self.graph:
            for v, capacity in self.graph[u].items():
                if parent[u] is not None and v not in parent and capacity == 0:
                    min_cut.add((u, v))
        return min_cut

flow_network = FlowNetwork()

flow_network.add_edge('A', 'B', 4)
flow_network.add_edge('A', 'C', 5)
flow_network.add_edge('B', 'C', 2)
flow_network.add_edge('B', 'D', 7)
flow_network.add_edge('C', 'D', 1)
flow_network.add_edge('C', 'E', 4)
flow_network.add_edge('D', 'E', 3)

source = 'A'
sink = 'E'

max_flow, min_cut = flow_network.ford_fulkerson(source, sink)

print(f"Maximum Flow: {max_flow}")