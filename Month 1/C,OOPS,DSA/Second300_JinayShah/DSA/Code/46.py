class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def construct_cartesian_tree(sequence):
    if not sequence:
        return None

    
    max_index = sequence.index(max(sequence))

    
    root = TreeNode(sequence[max_index])

    
    root.left = construct_cartesian_tree(sequence[:max_index])
    root.right = construct_cartesian_tree(sequence[max_index + 1:])

    return root

def in_order_traversal(node, result):
    if node:
        in_order_traversal(node.left, result)
        result.append(node.key)
        in_order_traversal(node.right, result)


def cartesian_tree_example():
    sequence = [3, 2, 6, 1, 9, 4, 7]
    
    
    root = construct_cartesian_tree(sequence)

    
    result = []
    in_order_traversal(root, result)

    print("Original Sequence:", sequence)
    print("In-order Traversal of Cartesian Tree:", result)

cartesian_tree_example()
