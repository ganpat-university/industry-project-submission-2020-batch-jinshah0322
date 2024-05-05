class Node:
    def __init__(self, key, value, rank=0, left=None, right=None):
        self.key = key
        self.value = value
        self.rank = rank
        self.left = left
        self.right = right

class WAVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return -1
        return node.rank

    def update_rank(self, node):
        if not node:
            return 0
        node.rank = 1 + max(self.height(node.left), self.height(node.right))
        return node.rank

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.update_rank(node)
        self.update_rank(new_root)
        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.update_rank(node)
        self.update_rank(new_root)
        return new_root

    def balance(self, node):
        if self.balance_factor(node) == 2:
            if self.balance_factor(node.left) == -1:
                node.left = self.rotate_left(node.left)
            node = self.rotate_right(node)
        elif self.balance_factor(node) == -2:
            if self.balance_factor(node.right) == 1:
                node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)
        return node

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if not node:
            return Node(key, value)
        
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value  

        self.update_rank(node)
        node = self.balance(node)

        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)


wavl_tree = WAVLTree()
wavl_tree.insert(10, "Value 1")
wavl_tree.insert(5, "Value 2")
wavl_tree.insert(15, "Value 3")

result = wavl_tree.search(5)
print(result)  
