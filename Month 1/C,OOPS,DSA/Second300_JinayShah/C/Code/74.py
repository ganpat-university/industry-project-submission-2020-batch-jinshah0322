def tarjan_dominators(graph, start):
    def dfs(u):
        nonlocal index
        index += 1
        dfn[u] = index
        idom[u] = dfn[u]
        ancestor[u] = u

        for v in graph[u]:
            if not dfn[v]:
                parent[v] = u
                dfs(v)

    def find(u):
        if ancestor[u] == u:
            return u
        root = find(ancestor[u])
        if dfn[idom[ancestor[u]]] < dfn[idom[u]]:
            idom[u] = idom[ancestor[u]]
        ancestor[u] = root
        return root

    def union(u, v):
        ancestor[v] = u

    n = len(graph)
    dfn = [0] * n
    idom = list(range(n))
    ancestor = list(range(n))
    parent = [-1] * n
    index = 0

    for node in graph.keys():
        if not dfn[node]:
            dfs(node)
    
    sorted_nodes = sorted(graph.keys(), key=lambda x: -dfn[x])

    for i in range(index, 1, -1):
        u = sorted_nodes[i - 1]
        for v in graph[u]:
            if dfn[v]:
                idom[v] = min(idom[v], idom[find(v)])

        if i > 1:
            u = sorted_nodes[i - 2]
            union(u, parent[u])

    return idom

graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
dominators = tarjan_dominators(graph, 0)
print("Dominators:", dominators)