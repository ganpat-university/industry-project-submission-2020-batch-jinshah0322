class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.mark = False

def dfs(node):
    if node is None or node.mark:
        return
    node.mark = True
    dfs(node.left)
    dfs(node.right)

def dsw(root):
    if root is None:
        return
    if root.mark:
        return
    root.mark = True
    dfs(root.left)
    dfs(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

dsw(root)

def display(node):
    if node is not None:
        display(node.left)
        if node.mark:
            print(node.value)
        display(node.right)

display(root)
