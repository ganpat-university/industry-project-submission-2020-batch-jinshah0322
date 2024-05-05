class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if(root.val==key):
            return root
        elif(root.val>key):
            root.left = insert(root.left,key)
        else:
            root.right = insert(root.right,key  )
        return root

def deletion(root,key):
    if root is None:
        return root
    if root.val > key:
        root.left = deletion(root.left,key)
        return root
    elif root.val<key:
        root.right=deletion(root.right,key)
        return root

    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp
    else:
        succParent = root
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
        root.key = succ.key
        del succ
        return root


def search(root,key):
    if(root is None or root.val==key):
        return root
    elif(root.val<key):
        return search(root.right,key)
    else:
        return search(root.left,key)
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
    
root = Node(10)
root = insert(root,20)
root = insert(root,5)
inorder(root)
root = deletion(root,5)
print()
inorder(root)