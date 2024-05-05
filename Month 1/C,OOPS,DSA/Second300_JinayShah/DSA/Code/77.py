class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class LayeredRangeTree2D:
    def __init__(self, points):
        self.root = self.construct_tree(points)

    def construct_tree(self, points):
        if not points:
            return None

        
        points.sort(key=lambda p: p.x)

        
        median_index = len(points) // 2
        median_point = points[median_index]

        left_points = [point for point in points if point.x < median_point.x]
        right_points = [point for point in points if point.x > median_point.x]

        return {
            'point': median_point,
            'left_child': self.construct_tree(left_points),
            'right_child': self.construct_tree(right_points)
        }

    def query_range(self, x_range, y_range):
        return self.query_range_recursive(self.root, x_range, y_range)

    def query_range_recursive(self, node, x_range, y_range):
        if node is None:
            return []

        result = []
        if x_range[0] <= node['point'].x <= x_range[1] and y_range[0] <= node['point'].y <= y_range[1]:
            result.append(node['point'])

        
        if node['left_child'] and x_range[0] <= node['left_child']['point'].x:
            result.extend(self.query_range_recursive(node['left_child'], x_range, y_range))

        if node['right_child'] and x_range[1] >= node['right_child']['point'].x:
            result.extend(self.query_range_recursive(node['right_child'], x_range, y_range))
        return result
points = [Point(2, 3), Point(5, 7), Point(8, 4), Point(9, 6), Point(10, 1)]
layered_tree = LayeredRangeTree2D(points)
query_result = layered_tree.query_range((3, 9), (2, 8))
for point in query_result:
    print(f"({point.x}, {point.y})")
