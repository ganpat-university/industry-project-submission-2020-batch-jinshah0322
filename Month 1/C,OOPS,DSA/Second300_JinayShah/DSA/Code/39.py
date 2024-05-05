import random

class TreapNode:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _insert(self, root, key, priority):
        if not root:
            return TreapNode(key, priority)

        if key < root.key:
            root.left = self._insert(root.left, key, priority)
            if root.left.priority > root.priority:
                root = self._rotate_right(root)
        else:
            root.right = self._insert(root.right, key, priority)
            if root.right.priority > root.priority:
                root = self._rotate_left(root)

        return root

    def insert(self, key):
        priority = random.randint(1, 1000)  
        self.root = self._insert(self.root, key, priority)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            if root.left.priority > root.right.priority:
                root = self._rotate_right(root)
                root.right = self._delete(root.right, key)
            else:
                root = self._rotate_left(root)
                root.left = self._delete(root.left, key)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _inorder_traversal(self, root):
        result = []

        if root:
            result.extend(self._inorder_traversal(root.left))
            result.append((root.key, root.priority))
            result.extend(self._inorder_traversal(root.right))

        return result

    def inorder_traversal(self):
        return self._inorder_traversal(self.root)


def treap_example():
    treap = Treap()

    keys_to_insert = [5, 2, 8, 1, 4, 7, 10]
    for key in keys_to_insert:
        treap.insert(key)

    print("Treap after insertion:")
    print(treap.inorder_traversal())

    key_to_delete = 4
    treap.delete(key_to_delete)

    print(f"Treap after deletion of key {key_to_delete}:")
    print(treap.inorder_traversal())

treap_example()
