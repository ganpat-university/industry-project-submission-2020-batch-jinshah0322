class TreeNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def height(node):
    return node.height if node else 0

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1

def balance_factor(node):
    return height(node.left) - height(node.right) if node else 0

def rotate_left(y):
    x = y.right
    T2 = x.left

    x.left = y
    y.right = T2

    update_height(y)
    update_height(x)

    return x

def rotate_right(x):
    y = x.left
    T2 = y.right

    y.right = x
    x.left = T2

    update_height(x)
    update_height(y)

    return y

def balance(node):
    if not node:
        return node

    update_height(node)

    # Left heavy
    if balance_factor(node) > 1:
        # Left-Right Case
        if balance_factor(node.left) < 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)

    # Right heavy
    if balance_factor(node) < -1:
        # Right-Left Case
        if balance_factor(node.right) > 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def insert(root, key):
    if not root:
        return TreeNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root  # Duplicate keys are not allowed

    return balance(root)

def delete(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Node with two children
        successor = find_min(root.right)
        root.key = successor.key
        root.right = delete(root.right, successor.key)

    return balance(root)

def find_min(node):
    while node.left:
        node = node.left
    return node

def search(root, key):
    if not root or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

# Example usage:
avl_tree = None

# Insert
avl_tree = insert(avl_tree, 10)
avl_tree = insert(avl_tree, 20)
avl_tree = insert(avl_tree, 30)

# Search
result = search(avl_tree, 20)
print("Search Result:", result.key if result else None)

# Delete
avl_tree = delete(avl_tree, 20)
result_after_deletion = search(avl_tree, 20)
print("Search Result After Deletion:", result_after_deletion.key if result_after_deletion else None)