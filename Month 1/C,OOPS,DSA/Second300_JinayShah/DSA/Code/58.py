class BlossomGraph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]
        self.match = [-1] * n
        self.in_blossom = [-1] * n
        self.blossom_parents = [-1] * n
        self.blossom_base = [-1] * n
        self.blossom_children = [[] for _ in range(n)]
        self.queue = []

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def find_augmenting_path(self, start):
        self.in_blossom = [-1] * self.n
        self.blossom_parents = [-1] * self.n
        self.blossom_base = [-1] * self.n
        self.blossom_children = [[] for _ in range(self.n)]
        self.queue = [start]
        self.in_blossom[start] = start

        while self.queue:
            u = self.queue.pop(0)
            for v in self.edges[u]:
                if self.in_blossom[v] == -1:
                    if self.match[v] == -1:
                        return self.construct_augmenting_path(start, v)
                    else:
                        self.in_blossom[v] = self.in_blossom[u]
                        self.blossom_parents[v] = u
                        self.blossom_base[v] = self.match[v]
                        self.queue.append(self.match[v])
                elif self.in_blossom[v] != self.in_blossom[u]:
                    return self.construct_augmenting_path(start, v)

    def construct_augmenting_path(self, start, end):
        path = [end]
        current = end

        while current != start:
            current = self.blossom_parents[current]
            path.append(current)

            if current == -1:
                break

        path.reverse()
        return path


    def augment_matching(self, path):
        for i in range(0, len(path) - 1, 2):
            u, v = path[i], path[i + 1]
            self.match[u] = v
            self.match[v] = u

    def contract_blossom(self, blossom_root, blossom_tip):
        blossom_base = self.blossom_base[blossom_root]
        blossom_children = self.blossom_children[blossom_root]

        for v in blossom_children:
            self.in_blossom[v] = -1
            self.blossom_parents[v] = -1
            self.blossom_base[v] = -1

        self.in_blossom[blossom_tip] = blossom_root
        self.blossom_parents[blossom_tip] = blossom_root
        self.blossom_base[blossom_tip] = blossom_base
        self.blossom_children[blossom_root].append(blossom_tip)


    def find_maximum_matching(self):
        for u in range(self.n):
            if self.match[u] == -1:
                augmenting_path = self.find_augmenting_path(u)
                if augmenting_path:
                    self.augment_matching(augmenting_path)

        return self.match


# Example usage:
if __name__ == "__main__":
    graph = BlossomGraph(6)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 0)

    maximum_matching = graph.find_maximum_matching()
    print("Maximum Cardinality Matching:", maximum_matching)
