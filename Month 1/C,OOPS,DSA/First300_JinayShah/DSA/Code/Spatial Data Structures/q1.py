class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QuadTreeNode:
    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.children = [None, None, None, None]  # NW, NE, SW, SE

class QuadTree:
    def __init__(self, boundary, capacity):
        self.root = QuadTreeNode(boundary, capacity)

    def insert(self, point):
        self._insert(self.root, point)

    def _insert(self, node, point):
        if not self._in_boundary(node.boundary, point):
            return

        if len(node.points) < node.capacity:
            node.points.append(point)
        else:
            if node.children[0] is None:
                self._subdivide(node)

            for child in node.children:
                self._insert(child, point)

    def _subdivide(self, node):
        x, y, w, h = node.boundary
        half_w, half_h = w / 2, h / 2

        node.children[0] = QuadTreeNode((x, y, half_w, half_h), node.capacity)  # NW
        node.children[1] = QuadTreeNode((x + half_w, y, half_w, half_h), node.capacity)  # NE
        node.children[2] = QuadTreeNode((x, y + half_h, half_w, half_h), node.capacity)  # SW
        node.children[3] = QuadTreeNode((x + half_w, y + half_h, half_w, half_h), node.capacity)  # SE

        for child in node.children:
            for p in node.points:
                self._insert(child, p)

        node.points = []

    def search(self, boundary):
        return self._search(self.root, boundary)

    def _search(self, node, boundary):
        result = []
        if not self._intersects(node.boundary, boundary):
            return result

        for point in node.points:
            if self._in_boundary(boundary, point):
                result.append(point)

        if node.children[0] is not None:
            for child in node.children:
                result.extend(self._search(child, boundary))

        return result

    def _intersects(self, boundary1, boundary2):
        x1, y1, w1, h1 = boundary1
        x2, y2, w2, h2 = boundary2
        return not (x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)

    def _in_boundary(self, boundary, point):
        x, y, w, h = boundary
        return x <= point.x <= x + w and y <= point.y <= y + h

boundary = (0, 0, 100, 100)
quadtree = QuadTree(boundary, capacity=4)

points_to_insert = [Point(10, 20), Point(30, 40), Point(70, 80), Point(90, 90)]
for point in points_to_insert:
    quadtree.insert(point)

search_boundary = (0, 0, 50, 50)
result = quadtree.search(search_boundary)

print("Points within search boundary:")
for point in result:
    print(f"({point.x}, {point.y})")