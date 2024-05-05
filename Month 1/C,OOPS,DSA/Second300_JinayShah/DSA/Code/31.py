class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class PersistentSegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.version_trees = [self._build_tree(0, len(arr) - 1)]

    def _build_tree(self, start, end):
        if start == end:
            return Node(self.arr[start])

        mid = (start + end) // 2
        left_child = self._build_tree(start, mid)
        right_child = self._build_tree(mid + 1, end)

        return Node(left=left_child, right=right_child, value=left_child.value + right_child.value)

    def _update_tree(self, node, start, end, index, value):
        if start == end == index:
            return Node(value)

        mid = (start + end) // 2
        if index <= mid:
            left_child = self._update_tree(node.left, start, mid, index, value)
            return Node(left=left_child, right=node.right, value=left_child.value + node.right.value)
        else:
            right_child = self._update_tree(node.right, mid + 1, end, index, value)
            return Node(left=node.left, right=right_child, value=node.left.value + right_child.value)

    def update(self, version, index, value):
        current_tree = self.version_trees[version]
        updated_tree = self._update_tree(current_tree, 0, len(self.arr) - 1, index, value)
        self.version_trees.append(updated_tree)

    def _query_tree(self, node, start, end, left, right):
        if start > right or end < left:
            return 0

        if left <= start and end <= right:
            return node.value

        mid = (start + end) // 2
        left_sum = self._query_tree(node.left, start, mid, left, right)
        right_sum = self._query_tree(node.right, mid + 1, end, left, right)

        return left_sum + right_sum

    def query(self, version, left, right):
        tree = self.version_trees[version]
        return self._query_tree(tree, 0, len(self.arr) - 1, left, right)


arr = [1, 3, 5, 7, 9]
pst = PersistentSegmentTree(arr)


pst.update(version=0, index=2, value=10)


result_version_0 = pst.query(version=0, left=1, right=4)
result_version_1 = pst.query(version=1, left=1, right=4)

print(f"Query result in version 0: {result_version_0}")
print(f"Query result in version 1: {result_version_1}")
