class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _splay(self, root, key):
        if not root:
            return None

        if key < root.key:
            if not root.left:
                return root

            if key < root.left.key:
                root.left.left = self._splay(root.left.left, key)
                root = self._right_rotate(root)
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right:
                    root.left = self._left_rotate(root.left)

            return root if not root.left else self._right_rotate(root)

        elif key > root.key:
            if not root.right:
                return root

            if key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left:
                    root.right = self._right_rotate(root.right)
            elif key > root.right.key:
                root.right.right = self._splay(root.right.right, key)
                root = self._left_rotate(root)

            return root if not root.right else self._left_rotate(root)

        else:
            return root

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self.root = self._splay(self.root, key)

            if key < self.root.key:
                new_node = Node(key)
                new_node.left = self.root.left
                new_node.right = self.root
                self.root.left = None
                self.root = new_node
            elif key > self.root.key:
                new_node = Node(key)
                new_node.right = self.root.right
                new_node.left = self.root
                self.root.right = None
                self.root = new_node

    def delete(self, key):
        if not self.root:
            return

        self.root = self._splay(self.root, key)

        if key == self.root.key:
            if not self.root.left:
                self.root = self.root.right
            else:
                right_subtree = self.root.right
                self.root = self.root.left
                self._splay(self.root, key)
                self.root.right = right_subtree

    def search(self, key):
        if not self.root:
            return False

        self.root = self._splay(self.root, key)
        return key == self.root.key


def main():
    splay_tree = SplayTree()

    elements_to_insert = [3, 7, 1, 5, 8, 2, 4, 6]

    for element in elements_to_insert:
        splay_tree.insert(element)

    
    search_key = 5
    print(f"Is {search_key} in the tree? {splay_tree.search(search_key)}")

    
    delete_key = 7
    splay_tree.delete(delete_key)
    print(f"Deleted {delete_key}. Is {delete_key} in the tree now? {splay_tree.search(delete_key)}")


if __name__ == "__main__":
    main()
