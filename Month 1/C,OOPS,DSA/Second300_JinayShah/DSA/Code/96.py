class OrderStatisticTreeNode:
    def __init__(self, key, size=1, left=None, right=None):
        self.key = key
        self.size = size  
        self.left = left
        self.right = right

def size(node):
    return node.size if node else 0

def build_order_statistic_tree(arr):
    root = None
    for value in arr:
        root = insert(root, value)
    return root

def insert(root, key):
    if not root:
        return OrderStatisticTreeNode(key)


    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.size = 1 + size(root.left) + size(root.right)
    return root

def kth_smallest(root, k):
    if not root or k <= 0 or k > root.size:
        return None

    left_size = size(root.left)
    if k == left_size + 1:
        return root.key
    elif k <= left_size:
        return kth_smallest(root.left, k)
    else:
        return kth_smallest(root.right, k - left_size - 1)


arr = [6, 5, 1, 4, 2]
order_stat_tree = build_order_statistic_tree(arr)


result = kth_smallest(order_stat_tree, 3)
print(f"The 3rd smallest element is: {result}")