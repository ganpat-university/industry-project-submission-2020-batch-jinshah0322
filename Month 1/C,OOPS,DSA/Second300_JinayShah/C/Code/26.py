from collections import defaultdict

class Graph:
   def __init__(self, vertices):
       self.V = vertices
       self.graph = defaultdict(list)
       self.Time = 0

   def addEdge(self, u, v):
       self.graph[u].append(v)

   def SCCUtil(self, u, disc, low, stackMember, st, result):
       disc[u] = self.Time
       low[u] = self.Time
       self.Time += 1
       stackMember[u] = True
       st.append(u)

       for v in self.graph[u]:
           if disc[v] == -1:
               self.SCCUtil(v, disc, low, stackMember, st, result)
               low[u] = min(low[u], low[v])
           elif stackMember[v]:
               low[u] = min(low[u], disc[v])

       w = -1
       component = []
       if low[u] == disc[u]:
           while w != u:
               w = st.pop()
               stackMember[w] = False
               component.append(w)

           result.append(component)

   def SCC(self):
       disc = [-1] * (self.V)
       low = [-1] * (self.V)
       stackMember = [False] * (self.V)
       st = []
       result = []

       for i in range(self.V):
           if disc[i] == -1:
               self.SCCUtil(i, disc, low, stackMember, st, result)

       print("Strongly Connected Components:")
       for component in result:
           print(component)

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.SCC()