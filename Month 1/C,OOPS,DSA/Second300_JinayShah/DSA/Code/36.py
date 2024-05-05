class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  

        self.update_height(root)

        balance = self.balance_factor(root)

        
        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        
        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        self.update_height(root)

        balance = self.balance_factor(root)

        
        if balance > 1:
            if self.balance_factor(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        
        if balance < -1:
            if self.balance_factor(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def get_min_value_node(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current

    def inorder_traversal(self, root):
        result = []

        if root:
            result.extend(self.inorder_traversal(root.left))
            result.append(root.key)
            result.extend(self.inorder_traversal(root.right))

        return result


def avl_tree_example():
    avl_tree = AVLTree()

    keys_to_insert = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for key in keys_to_insert:
        avl_tree.insert_key(key)

    print("AVL tree after insertion:")
    print(avl_tree.inorder_traversal(avl_tree.root))

    key_to_delete = 10
    avl_tree.delete_key(key_to_delete)

    print(f"AVL tree after deletion of key {key_to_delete}:")
    print(avl_tree.inorder_traversal(avl_tree.root))

avl_tree_example()
