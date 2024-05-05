class SegmentTree:
    def __init__(self, data):
        self.tree = [float('inf')] * (4 * len(data))
        self.build_tree(data, 1, 0, len(data) - 1)

    def build_tree(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self.build_tree(data, 2 * node, start, mid)
            self.build_tree(data, 2 * node + 1, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, left, right):
        if right < start or left > end:
            return float('inf')
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        left_min = self.query(2 * node, start, mid, left, right)
        right_min = self.query(2 * node + 1, mid + 1, end, left, right)
        return min(left_min, right_min)

data = [2, 5, 1, 4, 9, 3]
rmq_tree = SegmentTree(data)
result = rmq_tree.query(1, 0, len(data) - 1, 1, 4)
print("RMQ Result:", result)
