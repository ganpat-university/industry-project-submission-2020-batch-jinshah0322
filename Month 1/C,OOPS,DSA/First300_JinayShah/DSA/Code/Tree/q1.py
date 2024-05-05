class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inOrder(self,root):
        if(root):
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)

root = Node(10)        
root.insert(20)
root.insert(5)
root.insert(17)
root.insert(1)
root.inOrder(root)