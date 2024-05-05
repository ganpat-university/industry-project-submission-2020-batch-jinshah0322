class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        self.tree = [0] * (4 * self.size)
        self.lazy = [0] * (4 * self.size)

    def build_tree(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            self.build_tree(left_child, start, mid)
            self.build_tree(right_child, mid + 1, end)

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update_range(self, node, start, end, left, right, value):
        self.propagate(node, start, end)

        if start > end or start > right or end < left:
            return

        if left <= start and end <= right:
            self.tree[node] += (end - start + 1) * value

            if start != end:
                self.lazy[2 * node + 1] += value
                self.lazy[2 * node + 2] += value

        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2

            self.update_range(left_child, start, mid, left, right, value)
            self.update_range(right_child, mid + 1, end, left, right, value)

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query_range(self, node, start, end, left, right):
        self.propagate(node, start, end)

        if start > end or start > right or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        left_sum = self.query_range(left_child, start, mid, left, right)
        right_sum = self.query_range(right_child, mid + 1, end, left, right)

        return left_sum + right_sum

    def propagate(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]

            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]

            self.lazy[node] = 0



arr = [1, 3, 5, 7, 9, 11]
segment_tree = SegmentTree(arr)
segment_tree.build_tree(0, 0, len(arr) - 1)


query_left, query_right = 1, 4
result_query = segment_tree.query_range(0, 0, len(arr) - 1, query_left, query_right)
print(f"Sum in range [{query_left}, {query_right}] is {result_query}")


update_left, update_right, update_value = 1, 3, 2
segment_tree.update_range(0, 0, len(arr) - 1, update_left, update_right, update_value)


result_query_after_update = segment_tree.query_range(0, 0, len(arr) - 1, query_left, query_right)
print(f"Sum in range [{query_left}, {query_right}] after update is {result_query_after_update}")
