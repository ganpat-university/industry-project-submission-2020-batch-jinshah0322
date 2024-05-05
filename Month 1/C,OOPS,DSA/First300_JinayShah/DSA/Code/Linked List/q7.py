class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.count = 0
	def insert(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.count+=1
			return
		current_node = self.head
		while(current_node.next):
			current_node = current_node.next
		current_node.next = new_node
		self.count+=1
	def traverse(self):
		current_node = self.head
		while(current_node):
			print(current_node.data,end=" ")
			current_node = current_node.next
	def addition(self,llist1,llist2):
		currentNode1 = llist1.head
		currentNode2 = llist2.head
		while(currentNode1 and currentNode2):
			self.insert(currentNode1.data+currentNode2.data)
			currentNode1=currentNode1.next
			currentNode2=currentNode2.next
		

llist = LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.traverse()
llist1 = LinkedList()
print()
llist1.insert(5)
llist1.insert(6)
llist1.insert(7)
llist1.insert(8)
llist1.traverse()
print()
additionList = LinkedList()
additionList.addition(llist,llist1)
additionList.traverse()