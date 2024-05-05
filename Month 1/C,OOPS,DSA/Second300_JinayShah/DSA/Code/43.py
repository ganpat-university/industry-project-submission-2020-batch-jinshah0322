class SplayNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

class SplayTree:
    def __init__(self):
        self.root = None

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def _splay(self, node):
        while node.parent:
            parent = node.parent
            grandparent = parent.parent

            if not grandparent:
                if node == parent.left:
                    self._rotate_right(parent)
                else:
                    self._rotate_left(parent)
            elif node == parent.left and parent == grandparent.left:
                self._rotate_right(grandparent)
                self._rotate_right(parent)
            elif node == parent.right and parent == grandparent.right:
                self._rotate_left(grandparent)
                self._rotate_left(parent)
            elif node == parent.right and parent == grandparent.left:
                self._rotate_left(parent)
                self._rotate_right(grandparent)
            else:
                self._rotate_right(parent)
                self._rotate_left(grandparent)

    def insert(self, key):
        new_node = SplayNode(key)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while current:
                parent = current
                if key < current.key:
                    current = current.left
                else:
                    current = current.right

            if key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent

        self._splay(new_node)

    def search(self, key):
        current = self.root
        while current:
            if key == current.key:
                self._splay(current)
                return current.key
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None


def splay_tree_example():
    splay_tree = SplayTree()

    keys_to_insert = [3, 1, 4, 5, 2]
    for key in keys_to_insert:
        splay_tree.insert(key)

    search_key = 4
    result = splay_tree.search(search_key)

    print(f"Search result for key {search_key}: {result}")
    print("Splay tree after search:")
    
    inorder_traversal = splay_tree_inorder_traversal(splay_tree.root)
    print(inorder_traversal)

def splay_tree_inorder_traversal(node):
    result = []
    if node:
        result.extend(splay_tree_inorder_traversal(node.left))
        result.append(node.key)
        result.extend(splay_tree_inorder_traversal(node.right))
    return result

splay_tree_example()
