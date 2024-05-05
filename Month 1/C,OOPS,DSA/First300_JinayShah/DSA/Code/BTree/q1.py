class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode()
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode()
            self.root = new_root
            new_root.children.append(root)
            self.split_child(new_root, 0)
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

    def search(self, key, x=None):
        if x is None:
            x = self.root
        i = 0
        while i < len(x.keys) and key > x.keys[i]:
            i += 1
        if i < len(x.keys) and key == x.keys[i]:
            return True
        elif x.leaf:
            return False
        else:
            return self.search(key, x.children[i])

    def delete(self, key):
        root = self.root

        if not root.leaf and len(root.keys) == 1 and len(root.children) > 1:
            child = root.children[0]
            if len(child.keys) == self.t - 1:
                self.borrow_or_merge_from_sibling(root, 0)

        self.delete_key(root, key)

    def borrow_or_merge_from_sibling(self, x, i):
        t = self.t
        left_sibling = x.children[i]
        right_sibling = x.children[i + 1]

        if len(left_sibling.keys) >= t:
            x.keys[i] = left_sibling.keys.pop()
            if not left_sibling.leaf:
                transferred_child = left_sibling.children.pop()
                right_sibling.children.insert(0, transferred_child)
        elif len(right_sibling.keys) >= t:
            x.keys[i] = right_sibling.keys.pop(0)
            if not right_sibling.leaf:
                transferred_child = right_sibling.children.pop(0)
                left_sibling.children.append(transferred_child)
        else:
            merged_node = left_sibling
            merged_node.keys.append(x.keys.pop(i))
            merged_node.keys.extend(right_sibling.keys)
            merged_node.children.extend(right_sibling.children)
            x.children.pop(i + 1)

            if x == self.root and not x.keys:
                self.root = merged_node

    def delete_key(self, x, key):
        t = self.t
        i = 0
        while i < len(x.keys) and key > x.keys[i]:
            i += 1

        if i < len(x.keys) and key == x.keys[i]:
            if x.leaf:
                x.keys.pop(i)
            else:
                y = x.children[i]
                z = x.children[i + 1]

                if len(y.keys) >= t:
                    predecessor = self.get_predecessor(y)
                    x.keys[i] = predecessor
                    self.delete_key(y, predecessor)
                elif len(z.keys) >= t:
                    successor = self.get_successor(z)
                    x.keys[i] = successor
                    self.delete_key(z, successor)
                else:
                    x.keys.pop(i)
                    x.children.pop(i + 1)
                    y.keys.append(key)
                    y.keys.extend(z.keys)
                    y.children.extend(z.children)
                    if x == self.root and not x.keys:
                        self.root = y
                    self.delete_key(y, key)
        else:
            if x.leaf:
                print("Key not found:", key)
            else:
                child = x.children[i]
                if len(child.keys) == t - 1:
                    self.borrow_or_merge_from_sibling(x, i)
                self.delete_key(child, key)

    def get_predecessor(self, x):
        while not x.leaf:
            x = x.children[-1]
        return x.keys[-1]

    def get_successor(self, x):
        while not x.leaf:
            x = x.children[0]
        return x.keys[0]

btree = BTree(t=2)

keys_to_insert = [3, 8, 12, 5, 15, 2, 10, 6, 14, 9, 7]
for key in keys_to_insert:
    btree.insert(key)

print("B-tree after insertion:")
print("Root:", btree.root.keys)
for child in btree.root.children:
    print(child.keys)

key_to_search = 5
print(f"Search for key {key_to_search}")