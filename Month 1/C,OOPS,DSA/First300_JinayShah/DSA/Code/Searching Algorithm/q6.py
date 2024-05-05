from collections import defaultdict
class Graph:
    def __init__(self) :
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfsUtil(self,v,visited):
        visited.add(v)
        print(v,end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfsUtil(neighbour,visited)
    
    def DFS(self,v):
        visited = set()
        self.dfsUtil(v,visited)

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(3,4)
g.addEdge(2,4)

g.DFS(0)