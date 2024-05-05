class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    # Recursively build left and right subtrees
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])

    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val, end=" ")
        in_order_traversal(root.right)

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7]

balanced_bst = sorted_array_to_bst(sorted_array)

print("In-order Traversal of Balanced BST:")
in_order_traversal(balanced_bst)
