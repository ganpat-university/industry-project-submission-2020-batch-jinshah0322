import collections

class Graph:
  def __init__(self, edges):
      self.edges = collections.defaultdict(list)
      for u, v, w in edges:
          self.edges[u].append((v, w))
          self.edges[v].append((u, w))
      self.nodes_visited = set()
      self.nodes_to_check = []

  def boruvka_mst(self):
      num_nodes = len(self.edges)
      mst = []
      while len(mst) < num_nodes - 1:
          component_edges = []
          for node in self.edges:
              if node not in self.nodes_visited:
                self.nodes_visited.add(node)
                self.nodes_to_check = [node]
                while self.nodes_to_check:
                    node = self.nodes_to_check.pop()
                    for neighbor, weight in self.edges[node]:
                        if neighbor not in self.nodes_visited:
                            component_edges.append((node, neighbor, weight))
                            self.nodes_to_check.append(neighbor)
                            self.nodes_visited.add(neighbor)
          min_edge = min(component_edges, key=lambda edge: edge[2])
          mst.append(min_edge)
          self.nodes_visited.clear()
      return mst

edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
graph = Graph(edges)
print(graph.boruvka_mst())