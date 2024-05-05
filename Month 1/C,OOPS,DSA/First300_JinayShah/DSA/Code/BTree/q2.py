class BPlusTreeNode:
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.keys = []
        self.children = []
        self.next_leaf = None

class BPlusTree:
    def __init__(self, order):
        self.root = BPlusTreeNode()
        self.order = order

    def insert(self, key, value):
        root = self.root
        if len(root.keys) == 2 * self.order - 1:
            new_root = BPlusTreeNode(is_leaf=False)
            self.root = new_root
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, key, value)
        else:
            self.insert_non_full(root, key, value)

    def insert_non_full(self, x, key, value):
        i = len(x.keys) - 1

        if x.is_leaf:
            x.keys.append((key, value))
            x.keys.sort()
        else:
            while i >= 0 and key < x.keys[i][0]:
                i -= 1

            i += 1
            if len(x.children[i].keys) == 2 * self.order - 1:
                self.split_child(x, i)

                if key > x.keys[i][0]:
                    i += 1

            self.insert_non_full(x.children[i], key, value)

    def split_child(self, x, i):
        t = self.order
        y = x.children[i]
        z = BPlusTreeNode(is_leaf=y.is_leaf)

        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]

        if not y.is_leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

    def search(self, key, x=None):
        if x is None:
            x = self.root
        i = 0
        while i < len(x.keys) and key > x.keys[i][0]:
            i += 1
        if x.is_leaf:
            for k, v in x.keys:
                if key == k:
                    return v
            return None
        else:
            return self.search(key, x.children[i])

    def range_search(self, start_key, end_key):
        result = []
        node = self.find_leaf_node(start_key)

        while node is not None:
            for key, value in node.keys:
                if start_key <= key <= end_key:
                    result.append((key, value))
                elif key > end_key:
                    return result
            node = node.next_leaf

        return result

    def find_leaf_node(self, key):
        node = self.root
        while not node.is_leaf:
            i = 0
            while i < len(node.keys) and key >= node.keys[i][0]:
                i += 1
            node = node.children[i]
        return node

bplus_tree = BPlusTree(order=3)

key_value_pairs = [(3, 'A'), (8, 'B'), (12, 'C'), (5, 'D'), (15, 'E'), (2, 'F'), (10, 'G'), (6, 'H')]
for key, value in key_value_pairs:
    bplus_tree.insert(key, value)

search_key = 5
result = bplus_tree.search(search_key)
print(f"Search result for key {search_key}: {result}")

start_key, end_key = 4, 10
range_result = bplus_tree.range_search(start_key, end_key)
print(f"Range search result between {start_key} and {end_key}: {range_result}")