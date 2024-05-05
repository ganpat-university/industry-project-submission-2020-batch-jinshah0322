class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(postfix_expression):
    stack = []

    operators = set(['+', '-', '*', '/'])

    for token in postfix_expression:
        node = TreeNode(token)

        if token not in operators:
            stack.append(node)
        else:
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)

    return stack.pop()

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

postfix_expression = ['4', '5', '7', '*', '+', '3', '2', '*', '1', '+', '-']
expression_tree = build_expression_tree(postfix_expression)

print("Inorder Traversal of Expression Tree:")
inorder_traversal(expression_tree)
