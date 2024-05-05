class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert(head,data):
    newNode = Node(data)
    newNode.next = head
    if(head!=None):
        temp = head
        while(temp.next!=head):
            temp = temp.next
        temp.next = newNode
    else:
        newNode.next = newNode
    head = newNode
    return head

def traverse(head):
    if(head is None):
        print("List is empty")
        return 
    temp = head.next
    print(temp.data,end=" ")
    while(temp!=head):
        print(temp.data,end=" ")
        temp = temp.next
    print()

def removeNode(head,key):
    if(head is None):
        print("Empty list")
        return 
    if(head.data == key and head.next == head):
        head = None
        return
    temp = head
    if(head.data == key and head.next != head):
        while(temp.next!=head):
            temp = temp.next
        
        temp.next = head.next
        head = temp.next
        return 

    while(temp.next!=head and temp.next.data!=key):
        temp = temp.next
    if(temp.next.data == key):
        temp.next = temp.next.next
    else:
        print("There is no node for respective key")

head = None
head = insert(head,10)
head = insert(head,20)
head = insert(head,30)
head = insert(head,40)
head = insert(head,50)

traverse(head)
removeNode(head,40)
traverse(head)