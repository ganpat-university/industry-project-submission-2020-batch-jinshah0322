from collections import defaultdict

def sum_of_distances_in_tree(n, edges):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    count = [1] * n
    result = [0] * n

    def dfs1(node, parent):
        for child in tree[node]:
            if child != parent:
                dfs1(child, node)
                count[node] += count[child]
                result[node] += result[child] + count[child]

    def dfs2(node, parent):
        for child in tree[node]:
            if child != parent:
                result[child] = result[node] - count[child] + (n - count[child])
                dfs2(child, node)

    dfs1(0, -1)
    dfs2(0, -1)

    return result

num_nodes = 6
edges_list = [(0, 1), (0, 2), (2, 3), (2, 4), (2, 5)]
result_distances = sum_of_distances_in_tree(num_nodes, edges_list)
print("Sum of Distances:", result_distances)
