import networkx as nx

def minimum_cost_flow(graph, source, target, flow_demand):
    flow_dict = nx.network_simplex(graph)
    return flow_dict[0]  

G = nx.DiGraph()
G.add_edge('source', 'A', capacity=10, weight=2)
G.add_edge('source', 'B', capacity=5, weight=5)
G.add_edge('A', 'B', capacity=15, weight=1)
G.add_edge('A', 'target', capacity=10, weight=2)
G.add_edge('B', 'target', capacity=10, weight=4)

G.nodes['source']['demand'] = -5
G.nodes['A']['demand'] = 0
G.nodes['B']['demand'] = 0
G.nodes['target']['demand'] = 5

result = minimum_cost_flow(G, 'source', 'target', 15)
print(f"Minimum cost for the given flow demand: {result}")
