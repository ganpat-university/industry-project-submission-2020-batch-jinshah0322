class BTreeNode:
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    def __init__(self, t):
        self.root = BTreeNode()
        self.t = t

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(leaf=y.leaf)

        x.keys.insert(i, y.keys[t - 1])
        x.children.insert(i + 1, z)

        z.keys = y.keys[t:2 * t - 1]
        y.keys = y.keys[:t - 1]

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

    def insert(self, k):
        root = self.root
        t = self.t

        if len(root.keys) == 2 * t - 1:
            new_root = BTreeNode(leaf=False)
            self.root = new_root
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1

        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1

            i += 1
            if len(x.children[i].keys) == 2 * self.t - 1:
                self.split_child(x, i)

                if k > x.keys[i]:
                    i += 1

            self.insert_non_full(x.children[i], k)

    def delete(self, k):
        root = self.root

        if len(root.keys) == 1 and len(root.children) > 0:
            child = root.children[0]
            if len(child.keys) == 1:
                self.merge(root, 0)

        self.delete_key(root, k)

    def delete_key(self, x, k):
        t = self.t

        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1

        if i < len(x.keys) and k == x.keys[i]:
            self.delete_key_from_node(x, k, i)
        elif not x.leaf:
            self.delete_key_from_non_leaf(x, k, i)
        else:
            print(f"Key {k} not found in the tree.")

    def delete_key_from_node(self, x, k, i):
        if x.leaf:
            x.keys.pop(i)
        else:
            if len(x.children[i].keys) >= self.t:
                predecessor = self.get_predecessor(x, i)
                x.keys[i] = predecessor.keys.pop()
                self.delete_key(x.children[i], predecessor.keys[-1])
            elif len(x.children[i + 1].keys) >= self.t:
                successor = self.get_successor(x, i)
                x.keys[i] = successor.keys.pop(0)
                self.delete_key(x.children[i + 1], successor.keys[0])
            else:
                self.merge(x, i)
                self.delete_key(x.children[i], k)

    def delete_key_from_non_leaf(self, x, k, i):
        t = self.t
        if len(x.children[i].keys) == t - 1:
            if i > 0 and len(x.children[i - 1].keys) >= t:
                self.borrow_from_prev(x, i)
            elif i < len(x.keys) and len(x.children[i + 1].keys) >= t:
                self.borrow_from_next(x, i)
            elif i > 0:
                self.merge(x, i - 1)
            else:
                self.merge(x, i)

        self.delete_key(x.children[i], k)

    def get_predecessor(self, x, i):
        x = x.children[i]
        while not x.leaf:
            x = x.children[-1]
        return x

    def get_successor(self, x, i):
        x = x.children[i + 1]
        while not x.leaf:
            x = x.children[0]
        return x

    def borrow_from_prev(self, x, i):
        child = x.children[i]
        sibling = x.children[i - 1]

        child.keys.insert(0, x.keys[i - 1])
        x.keys[i - 1] = sibling.keys.pop()

        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

    def borrow_from_next(self, x, i):
        child = x.children[i]
        sibling = x.children[i + 1]

        child.keys.append(x.keys[i])
        x.keys[i] = sibling.keys.pop(0)

        if not child.leaf:
            child.children.append(sibling.children.pop(0))

    def merge(self, x, i):
        child = x.children[i]
        sibling = x.children[i + 1]

        child.keys.append(x.keys.pop(i))
        child.keys += sibling.keys

        if not child.leaf:
            child.children += sibling.children

        x.children.pop(i + 1)


def b_tree_example():
    b_tree = BTree(t=2)

    keys_to_insert = [3, 8, 5, 9, 7, 1, 2, 6, 4]
    for key in keys_to_insert:
        b_tree.insert(key)

    print("B-tree after insertion:")
    print(b_tree.root.keys)

    key_to_delete = 6
    b_tree.delete(key_to_delete)

    print(f"B-tree after deletion of key {key_to_delete}:")
    print(b_tree.root.keys)

b_tree_example()
