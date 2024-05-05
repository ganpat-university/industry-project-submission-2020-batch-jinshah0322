import random

class ScapegoatTreeNode:
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

class ScapegoatTree:
    def __init__(self, alpha=0.75):
        self.root = None
        self.alpha = alpha  

    def insert(self, key):
        if not self.root:
            self.root = ScapegoatTreeNode(key)
        else:
            self._insert(self.root, key)
            if self._depth(self.root) > 1.5 * self._log_size(self.root):
                
                self.root = self._rebuild_tree(self.root)

    def _insert(self, node, key):
        if key < node.key:
            if node.left:
                self._insert(node.left, key)
            else:
                node.left = ScapegoatTreeNode(key, node)
        elif key > node.key:
            if node.right:
                self._insert(node.right, key)
            else:
                node.right = ScapegoatTreeNode(key, node)

    def _depth(self, node):
        if not node:
            return 0
        return 1 + max(self._depth(node.left), self._depth(node.right))

    def _log_size(self, node):
        if not node:
            return 0
        return 1 + self._log_size(node.left) + self._log_size(node.right)

    def _in_order_traversal(self, node):
        if node:
            yield from self._in_order_traversal(node.left)
            yield node.key
            yield from self._in_order_traversal(node.right)

    def _sorted_keys(self):
        return list(self._in_order_traversal(self.root))

    def _rebuild_tree(self, node):
        sorted_keys = self._sorted_keys()
        return self._build_tree_from_sorted_keys(sorted_keys)

    def _build_tree_from_sorted_keys(self, keys):
        if not keys:
            return None
        mid = len(keys) // 2
        node = ScapegoatTreeNode(keys[mid])
        node.left = self._build_tree_from_sorted_keys(keys[:mid])
        node.right = self._build_tree_from_sorted_keys(keys[mid + 1:])
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)


scapegoat_tree = ScapegoatTree()


keys_to_insert = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
for key in keys_to_insert:
    scapegoat_tree.insert(key)


search_key = 7
print(f"Is {search_key} in the tree? {scapegoat_tree.search(search_key)}")
