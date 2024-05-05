import bisect

class BPlusTree:
    def __init__(self, order, block_size):
        self.order = order
        self.block_size = block_size
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = LeafNode()
        self.root.insert(key, value)

    def search(self, key):
        if self.root is not None:
            return self.root.search(key)
        return None

class Node:
    def __init__(self):
        self.keys = []
        self.children = []

    def is_leaf(self):
        return not bool(self.children)

    def insert(self, key, value):
        pass

    def search(self, key):
        pass

class InternalNode(Node):
    def insert(self, key, value):
        index = bisect.bisect_left(self.keys, key)
        child = self.children[index]
        child.insert(key, value)

    def search(self, key):
        index = bisect.bisect_right(self.keys, key) - 1
        return self.children[index].search(key)

class LeafNode(Node):
    def insert(self, key, value):
        index = bisect.bisect_left(self.keys, key)
        self.keys.insert(index, key)
        self.children.insert(index, value)

    def search(self, key):
        index = bisect.bisect_left(self.keys, key)
        if index < len(self.keys) and self.keys[index] == key:
            return self.children[index]
        return None


tree = BPlusTree(order=3, block_size=4096)
tree.insert(10, "Data1")
tree.insert(5, "Data2")
tree.insert(15, "Data3")
result = tree.search(5)
print(result)  
