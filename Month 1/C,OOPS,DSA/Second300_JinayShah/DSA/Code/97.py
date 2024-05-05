class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.size = 1
        self.left = None
        self.right = None

def cartesian_tree_insert(root, key, priority):
    if root is None:
        return Node(key, priority)

    if key < root.key:
        root.left = cartesian_tree_insert(root.left, key, priority)
    else:
        root.right = cartesian_tree_insert(root.right, key, priority)

    root.size = 1 + (root.left.size if root.left else 0) + (root.right.size if root.right else 0)
    return root

def cartesian_tree_query(root, key):
    if root is None:
        return None

    if key == root.key:
        return root
    elif key < root.key:
        return cartesian_tree_query(root.left, key)
    else:
        return cartesian_tree_query(root.right, key)

root_version_1 = None
root_version_2 = None

elements_version_1 = [3, 1, 4, 5, 2]
for element in elements_version_1:
    root_version_1 = cartesian_tree_insert(root_version_1, element, priority=element)

elements_version_2 = [6, 7, 8]
for element in elements_version_2:
    root_version_2 = cartesian_tree_insert(root_version_2, element, priority=element)

query_key = 5
result_version_1 = cartesian_tree_query(root_version_1, query_key)
result_version_2 = cartesian_tree_query(root_version_2, query_key)

print(f"Querying key {query_key} at time 1: {result_version_1.key if result_version_1 else None}")
print(f"Querying key {query_key} at time 2: {result_version_2.key if result_version_2 else None}")
