class Node:
    def __init__(self, key, index):
        self.key = key
        self.index = index
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    root = None
    stack = []

    for i, key in enumerate(arr):
        node = Node(key, i)

        while stack and stack[-1].key > key:
            node.left = stack.pop()

        if stack:
            stack[-1].right = node
        else:
            root = node

        stack.append(node)

    return root

def query_min(root, start, end):
    if not root:
        return float('inf')

    if root.index >= start and root.index <= end:
        return root.key

    if root.index < start:
        return query_min(root.right, start, end)

    if root.index > end:
        return query_min(root.left, start, end)

def range_minimum_query(arr, queries):
    cartesian_tree = build_cartesian_tree(arr)
    results = []

    for query in queries:
        start, end = query
        min_value = query_min(cartesian_tree, start, end)
        results.append(min_value)

    return results


arr = [3, 1, 4, 5, 2]
queries = [(1, 3), (0, 4), (2, 4)]

result = range_minimum_query(arr, queries)
print("Results:", result)
