class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    if not points:
        return None

    k = len(points[0])
    axis = depth % k

    sorted_points = sorted(points, key=lambda x: x[axis])
    median = len(sorted_points) // 2

    return Node(
        point=sorted_points[median],
        left=build_kd_tree(sorted_points[:median], depth + 1),
        right=build_kd_tree(sorted_points[median + 1:], depth + 1)
    )

def search_minimum_kd_tree(root, depth=0):
    if root is None:
        return None

    k = len(root.point)
    axis = depth % k

    if root.left is None:
        return root.point[axis]

    return search_minimum_kd_tree(root.left, depth + 1)


points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
kd_tree = build_kd_tree(points)


min_value = search_minimum_kd_tree(kd_tree)
print(f"The minimum value in the KD-Tree is: {min_value}")
