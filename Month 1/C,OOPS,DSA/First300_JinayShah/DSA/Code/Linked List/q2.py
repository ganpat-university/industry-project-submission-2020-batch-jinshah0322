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
			print(current_node.data)
			current_node = current_node.next
	def midElement(self):
		mid = self.count//2
		current_node = self.head
		while(mid!=0):
			current_node = current_node.next
			mid-=1
		print(f"Middle element is {current_node.data}")

llist = LinkedList()
llist.insert('a')
llist.insert('b')
llist.insert('c')
llist.insert('d')
llist.traverse()
llist.midElement()