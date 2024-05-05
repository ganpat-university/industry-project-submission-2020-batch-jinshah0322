class Node:
    def __init__(self, point, depth, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right
        self.depth = depth

def kdtree(points, depth=0):
    if not points:
        return None

    k = len(points[0])
    axis = depth % k

    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    return Node(
        point=points[median],
        depth=depth,
        left=kdtree(points[:median], depth + 1),
        right=kdtree(points[median + 1:], depth + 1)
    )

def kdtree_search(root, target, depth=0):
    if root is None:
        return None

    k = len(target)
    axis = depth % k

    if target == root.point:
        return root.point
    elif target[axis] < root.point[axis]:
        return kdtree_search(root.left, target, depth + 1)
    else:
        return kdtree_search(root.right, target, depth + 1)

points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
kdtree_root = kdtree(points)

target_point = (9, 6)
result = kdtree_search(kdtree_root, target_point)

print(f"Target point {target_point} found in the K-D tree: {result}")