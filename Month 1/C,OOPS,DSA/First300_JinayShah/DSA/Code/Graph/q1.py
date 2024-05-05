class SimpleGraph:
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
            
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
    
    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]
            for v in self.vertices:
                self.vertices[v] = [vtx for vtx in self.vertices[v] if vtx != vertex]
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1] = [vtx for vtx in self.vertices[vertex1] if vtx != vertex2]
            self.vertices[vertex2] = [vtx for vtx in self.vertices[vertex2] if vtx != vertex1]
    
    def display_graph(self):
        for vertex in self.vertices:
            print(f"{vertex}: {self.vertices[vertex]}")

graph = SimpleGraph()

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.display_graph()
graph.remove_vertex(2)
graph.display_graph()
graph.add_vertex(4)
graph.add_edge(1, 4)
graph.display_graph()
graph.remove_edge(1, 4)
graph.display_graph()