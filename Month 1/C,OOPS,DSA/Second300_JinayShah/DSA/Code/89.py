class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.link_cut_parent = None
        self.subtree_sum = value  

def make_tree(value):
    return Node(value)

def find_root(x):
    while x is not None and x.parent is not None:
        x = x.parent
    return x

def expose(x):
    last = None
    while x is not None:
        splay(x)
        x.right = last
        update_subtree_sum(x)
        last = x
        x = x.link_cut_parent

def splay(x):
    while x.parent is not None:
        if x.parent.parent is None:
            if x.parent.left == x:
                rotate_right(x.parent)
            else:
                rotate_left(x.parent)
        elif (x.parent.left == x) == (x.parent.parent.left == x.parent):
            if x.parent.left == x:
                rotate_right(x.parent.parent)
                rotate_right(x.parent)
            else:
                rotate_left(x.parent.parent)
                rotate_left(x.parent)
        else:
            if x.parent.left == x:
                rotate_right(x.parent)
                rotate_left(x.parent)
            else:
                rotate_left(x.parent)
                rotate_right(x.parent)

def rotate_right(x):
    y = x.left
    if y is not None:
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.right = x
        y.parent = x.parent
        x.parent = y
        update_subtree_sum(x)
        update_subtree_sum(y)

def rotate_left(x):
    y = x.right
    if y is not None:
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.left = x
        y.parent = x.parent
        x.parent = y
        update_subtree_sum(x)
        update_subtree_sum(y)

def link(x, y):
    expose(y)
    y.link_cut_parent = x

def cut(x):
    expose(x)
    if x.left is not None:
        x.left.parent = None
    x.left = None
    update_subtree_sum(x)

def update_subtree_sum(x):
    x.subtree_sum = x.value
    if x.left is not None:
        x.subtree_sum += x.left.subtree_sum
    if x.right is not None:
        x.subtree_sum += x.right.subtree_sum

def query_path_sum(x):
    expose(x)
    return x.subtree_sum



nodes = [make_tree(i + 1) for i in range(5)]


for i in range(4):
    link(nodes[i], nodes[i + 1])


result = query_path_sum(nodes[4])
print("Path sum from leaf to root:", result)  


cut(nodes[2])


result = query_path_sum(nodes[3])
print("Path sum from nodes[3] to root:", result)  
