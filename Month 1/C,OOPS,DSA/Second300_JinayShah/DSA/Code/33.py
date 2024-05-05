class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def find_parent(self, parent, node):
        if parent[node] == node:
            return node
        return self.find_parent(parent, parent[node])

    def union(self, parent, rank, u, v):
        root_u = self.find_parent(parent, u)
        root_v = self.find_parent(parent, v)

        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

    def kruskal(self):
        result = []
        self.edges = sorted(self.edges, key=lambda edge: edge[2])

        parent = [i for i in range(self.vertices)]
        rank = [0] * self.vertices

        for edge in self.edges:
            u, v, weight = edge
            root_u = self.find_parent(parent, u)
            root_v = self.find_parent(parent, v)

            if root_u != root_v:
                result.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

        return result


def kruskal_example():
    g = Graph(4)

    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    mst = g.kruskal()

    print("Minimum Spanning Tree:")
    for edge in mst:
        print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")

kruskal_example()
