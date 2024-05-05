class IntervalTree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

def insert(root, start, end):
    if root is None:
        return IntervalTree(start, end)

    if start < root.start:
        root.left = insert(root.left, start, end)
    else:
        root.right = insert(root.right, start, end)

    return root

def delete(root, start, end):
    if root is None:
        return None

    if end < root.start:
        root.left = delete(root.left, start, end)
    elif start > root.end:
        root.right = delete(root.right, start, end)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            successor = find_min(root.right)
            root.start, root.end = successor.start, successor.end
            root.right = delete(root.right, successor.start, successor.end)

    return root

def search(root, start, end):
    result = []
    if root:
        if start <= root.end and end >= root.start:
            result.append((root.start, root.end))
        if start < root.start:
            result.extend(search(root.left, start, end))
        if end > root.end:
            result.extend(search(root.right, start, end))

    return result

def find_min(node):
    while node.left:
        node = node.left
    return node

intervals = [(15, 20), (10, 30), (5, 12), (25, 40)]

root = None
for start, end in intervals:
    root = insert(root, start, end)

query_start, query_end = (14, 26)
result = search(root, query_start, query_end)
print(f"Intervals overlapping with ({query_start}, {query_end}): {result}")

delete_start, delete_end = 15, 20
root = delete(root, delete_start, delete_end)

result = search(root, query_start, query_end)
print(f"Intervals overlapping with ({query_start}, {query_end}): {result}")
