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

def insert_kd_tree(root, point, depth=0):
    if root is None:
        return Node(point)

    k = len(point)
    axis = depth % k

    if point[axis] < root.point[axis]:
        root.left = insert_kd_tree(root.left, point, depth + 1)
    else:
        root.right = insert_kd_tree(root.right, point, depth + 1)

    return root

def search_kd_tree(root, target, depth=0):
    if root is None:
        return None

    k = len(target)
    axis = depth % k

    if root.point == target:
        return root.point

    if target[axis] < root.point[axis]:
        return search_kd_tree(root.left, target, depth + 1)
    else:
        return search_kd_tree(root.right, target, depth + 1)


points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
kd_tree = build_kd_tree(points)


target_point = (5, 4)
result = search_kd_tree(kd_tree, target_point)
print(f"Point {target_point} found in the KD-Tree: {result}")


new_point = (6, 3)
kd_tree = insert_kd_tree(kd_tree, new_point)


result_after_insert = search_kd_tree(kd_tree, new_point)
print(f"Point {new_point} found in the KD-Tree after insertion: {result_after_insert}")
