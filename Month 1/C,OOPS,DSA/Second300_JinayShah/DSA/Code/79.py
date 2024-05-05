class Node:
    def __init__(self, key, value, color, left=None, right=None):
        self.key = key
        self.value = value
        self.color = color
        self.left = left
        self.right = right

class PersistentRedBlackTree:
    def __init__(self):
        self.versions = {}  
        self.current_version = 0

    def insert(self, key, value):
        root = self.get_version(self.current_version)
        new_root = self._insert(root, key, value)
        self.current_version += 1
        self.versions[self.current_version] = new_root

    def _insert(self, node, key, value):
        if not node:
            return Node(key, value, color=1)  

        if key < node.key:
            left = self._insert(node.left, key, value)
            return self.balance(Node(node.key, node.value, color=node.color, left=left, right=node.right))
        elif key > node.key:
            right = self._insert(node.right, key, value)
            return self.balance(Node(node.key, node.value, color=node.color, left=node.left, right=right))
        else:
            
            return Node(key, value, color=node.color, left=node.left, right=node.right)

    def search(self, key, version=None):
        if version is None:
            version = self.current_version
        root = self.get_version(version)
        return self._search(root, key)

    def _search(self, node, key):
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None

    def balance(self, node):
        
        return node

    def get_version(self, version):
        return self.versions.get(version, None)

# Example usage:
persistent_tree = PersistentRedBlackTree()
persistent_tree.insert(10, "Version 1")
persistent_tree.insert(20, "Version 1")
persistent_tree.insert(30, "Version 1")
persistent_tree.insert(15, "Version 2")
persistent_tree.insert(25, "Version 2")

result_v1 = persistent_tree.search(15, version=1)
result_v2 = persistent_tree.search(15, version=2)

print(result_v1)  
print(result_v2)  