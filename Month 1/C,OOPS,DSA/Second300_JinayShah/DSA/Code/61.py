class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.reverse = False

def make_tree(key):
    return Node(key)

def link(x, y):
    make_root(x)
    x.parent = y
    
def cut(x):
    expose(x)
    if x.left:
        x.left.parent = None
        x.left = None

def find_root(x):
    expose(x)
    while x.right:
        x = x.right
    splay(x)
    return x

def expose(x):
    last = None

    while x:
        splay(x)
        x.right = last
        last = x

        x = x.parent

def make_root(x):
    expose(x)
    splay(x)
    x.reverse = not x.reverse

def splay(x):
    while x.parent:
        y = x.parent
        z = y.parent

        if not z:
            rotate(x)
        elif (y.left == x) == (z.left == y):
            rotate(y)
            rotate(x)
        else:
            rotate(x)
            rotate(x)

def rotate(x):
    y = x.parent

    if not y.parent:
        pass
    elif y.left == x:
        y.parent.left = x
    else:
        y.parent.right = x

    x.parent = y.parent
    y.parent = x

    if x.parent:
        if x.parent.left == y:
            x.parent.left = x
        else:
            x.parent.right = x

def main():
    
    nodes = [make_tree(i) for i in range(1, 6)]

    link(nodes[1], nodes[2])
    link(nodes[2], nodes[3])
    link(nodes[3], nodes[4])

    print("Root of the tree after linking nodes 1, 2, 3, 4:", find_root(nodes[1]).key)

    cut(nodes[3])

    print("Root of the tree after cutting node 3:", find_root(nodes[1]).key)

    make_root(nodes[2])

    print("Root of the tree after making node 2 the root:", find_root(nodes[2]).key)

if __name__ == "__main__":
    main()
