class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def has_cycle(self):
        visited = set()
        recursion_stack = set()

        def is_cyclic(vertex):
            visited.add(vertex)
            recursion_stack.add(vertex)

            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    if is_cyclic(neighbor):
                        return True
                elif neighbor in recursion_stack:
                    return True

            recursion_stack.remove(vertex)
            return False

        for vertex in self.graph:
            if vertex not in visited:
                if is_cyclic(vertex):
                    return True

        return False

my_graph = Graph()

my_graph.add_edge(1, 2)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 1)

has_cycle = my_graph.has_cycle()

if has_cycle:
    print("The graph has a cycle.")
else:
    print("The graph does not have a cycle.")
