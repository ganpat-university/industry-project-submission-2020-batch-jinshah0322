class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node
            right_child = 2 * node + 1

            self.build(left_child, start, mid)
            self.build(right_child, mid + 1, end)

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, node, start, end, query_start, query_end):
        if start > query_end or end < query_start:
            return 0

        if query_start <= start and end <= query_end:
            return self.tree[node]

        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1

        left_sum = self.query(left_child, start, mid, query_start, query_end)
        right_sum = self.query(right_child, mid + 1, end, query_start, query_end)

        return left_sum + right_sum

    def range_query(self, query_start, query_end):
        return self.query(1, 0, self.n - 1, query_start, query_end)


arr = [1, 2, 3, 4, 5, 6, 7, 8]
seg_tree = SegmentTree(arr)

result = seg_tree.range_query(2, 5)
print("Sum in range [2, 5]:", result)