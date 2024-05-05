class BTreeNode:
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    def __init__(self, t):
        self.root = BTreeNode()
        self.t = t

    def range_query(self, node, start_range, end_range, result):
        i = 0
        while i < len(node.keys) and start_range > node.keys[i]:
            i += 1

        while i < len(node.keys) and start_range <= node.keys[i] <= end_range:
            result.append(node.keys[i])
            i += 1

        if not node.leaf:
            for j in range(i):
                self.range_query(node.children[j], start_range, end_range, result)
            if i < len(node.children):
                self.range_query(node.children[i], start_range, end_range, result)

    def search_range(self, start_range, end_range):
        result = []
        self.range_query(self.root, start_range, end_range, result)
        return result

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, x, key):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and key < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = key
        else:
            while i >= 0 and key < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if key > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], key)

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(leaf=y.leaf)

        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(2 * t) - 1]
        y.keys = y.keys[0:t - 1]

        if not y.leaf:
            z.children = y.children[t:2 * t]
            y.children = y.children[0:t - 1]


btree = BTree(t=2)

elements_to_insert = [3, 9, 7, 1, 8, 4, 5, 6, 2]
for element in elements_to_insert:
    btree.insert(element)

start_range = 4
end_range = 7
result_range_query = btree.search_range(start_range, end_range)

print(f"Elements in the range [{start_range}, {end_range}]: {result_range_query}")
