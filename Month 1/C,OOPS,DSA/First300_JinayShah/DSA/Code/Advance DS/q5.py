class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
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

    def update(self, node, start, end, update_start, update_end, value):
        self.lazy_update(node, start, end)

        if start > update_end or end < update_start:
            return

        if update_start <= start and end <= update_end:
            self.tree[node] += (end - start + 1) * value

            if start != end:
                self.lazy[node * 2] += value
                self.lazy[node * 2 + 1] += value

            return

        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1

        self.update(left_child, start, mid, update_start, update_end, value)
        self.update(right_child, mid + 1, end, update_start, update_end, value)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def range_update(self, update_start, update_end, value):
        self.update(1, 0, self.n - 1, update_start, update_end, value)

    def query(self, node, start, end, query_start, query_end):
        self.lazy_update(node, start, end)

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

    def lazy_update(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]

            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]

            self.lazy[node] = 0

arr = [1, 2, 3, 4, 5, 6, 7, 8]
seg_tree = SegmentTree(arr)

seg_tree.range_update(2, 5, 3)

result = seg_tree.query(1, 0, len(arr) - 1, 2, 5)
print("Sum in range [2, 5]:", result)