class Node:
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []

class PersistentBTree:
    def __init__(self, order):
        self.order = order
        self.versions = {}  
        self.current_version = 0

    def _insert(self, node, key):
        index = len(node.keys) - 1
        while index >= 0 and key < node.keys[index]:
            index -= 1

        index += 1

        if node.is_leaf:
            node.keys.insert(index, key)
        else:
            child = node.children[index]
            if len(child.keys) == (2 * self.order) - 1:
                self._split_child(node, index, child)
                if key > node.keys[index]:
                    index += 1
            self._insert(node.children[index], key)

    def _split_child(self, parent, index, child):
        new_child = Node(is_leaf=child.is_leaf)
        split_index = self.order - 1

        parent.keys.insert(index, child.keys[split_index])
        parent.children.insert(index + 1, new_child)

        new_child.keys = child.keys[split_index + 1:]
        child.keys = child.keys[:split_index]

        if not child.is_leaf:
            new_child.children = child.children[split_index + 1:]
            child.children = child.children[:split_index + 1]

    def insert(self, key):
        root = self.get_version(self.current_version)
        if len(root.keys) == (2 * self.order) - 1:
            new_root = Node(is_leaf=False)
            new_root.children.append(root)
            self._split_child(new_root, 0, root)
            self.root = new_root
            self.current_version += 1
        self._insert(self.get_version(self.current_version), key)

    def get_version(self, version):
        if version not in self.versions:
            self.versions[version] = Node()
        return self.versions[version]

def main():
    btree = PersistentBTree(order=2)

    
    elements_to_insert = [3, 7, 1, 5, 8, 2, 4, 6]
    for element in elements_to_insert:
        btree.insert(element)

    
    print("Current B-tree:")
    print_tree(btree.get_version(btree.current_version))

    
    btree.insert(9)
    print("\nUpdated B-tree:")
    print_tree(btree.get_version(btree.current_version))

    
    print("\nPrevious B-tree version:")
    print_tree(btree.get_version(btree.current_version - 1))

def print_tree(node, level=0):
    if node:
        print(f"Level {level}: {node.keys}")
        if not node.is_leaf:
            for child in node.children:
                print_tree(child, level + 1)

if __name__ == "__main__":
    main()
