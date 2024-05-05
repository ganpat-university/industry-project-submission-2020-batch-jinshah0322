class Node:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None
        self.lazy = 0

class PersistentSegmentTree:
    def __init__(self, arr):
        self.version_roots = [None]
        self.arr = arr
        self.n = len(arr)

    def build(self, start, end):
        if start == end:
            return Node(self.arr[start])

        mid = (start + end) // 2
        left_child = self.build(start, mid)
        right_child = self.build(mid + 1, end)

        node = Node(left_child.value + right_child.value)
        node.left = left_child
        node.right = right_child

        return node

    def update(self, version, start, end, range_start, range_end, delta):
        if start > range_end or end < range_start:
            return self.version_roots[version]

        if not self.version_roots[version]:
            self.version_roots[version] = self.build(0, self.n - 1)

        if start == end:
            new_root = Node(self.version_roots[version].value + delta)
            new_root.lazy = self.version_roots[version].lazy
            return new_root

        mid = (start + end) // 2
        left_child = self.update(version, start, mid, range_start, range_end, delta)
        right_child = self.update(version, mid + 1, end, range_start, range_end, delta)

        new_root = Node(left_child.value + right_child.value)
        new_root.left = left_child
        new_root.right = right_child

        return new_root

    def query(self, version, start, end, range_start, range_end):
        if not self.version_roots[version] or start > range_end or end < range_start:
            return 0

        if start == end or (range_start <= start and end <= range_end):
            return self.version_roots[version].value + self.version_roots[version].lazy * (end - start + 1)

        mid = (start + end) // 2

        
        if self.version_roots[version].lazy != 0:
            self.version_roots[version].left = self.update_lazy(self.version_roots[version].left, start, mid, self.version_roots[version].lazy)
            self.version_roots[version].right = self.update_lazy(self.version_roots[version].right, mid + 1, end, self.version_roots[version].lazy)
            self.version_roots[version].lazy = 0

        left_sum = self.query(version, start, mid, range_start, range_end)
        right_sum = self.query(version, mid + 1, end, range_start, range_end)

        return left_sum + right_sum

    def update_lazy(self, node, start, end, delta):
        if not node:
            return None

        new_node = Node(node.value + delta * (end - start + 1))
        new_node.lazy = node.lazy + delta
        new_node.left = self.update_lazy(node.left, start, (start + end) // 2, delta)
        new_node.right = self.update_lazy(node.right, (start + end) // 2 + 1, end, delta)

        return new_node

    def update_range(self, version, range_start, range_end, delta):
        root = self.version_roots[version]
        new_root = self.update(version, 0, self.n - 1, range_start, range_end, delta)
        self.version_roots.append(new_root)


arr = [1, 2, 3, 4, 5]
pst = PersistentSegmentTree(arr)


pst.version_roots[0] = pst.build(0, pst.n - 1)


pst.update_range(0, 1, 3, 2)


pst.update_range(1, 0, 4, 1)


result_original = pst.query(0, 0, pst.n - 1, 0, 4)


result_after_update = pst.query(1, 0, pst.n - 1, 0, 4)

print("Sum in the original array:", result_original)  
print("Sum after the update:", result_after_update)  
