class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	def insert(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return self.head
		current_node = self.head
		while(current_node.next):
			current_node = current_node.next
		current_node.next = new_node
	def loop(self):
		s =set()
		current_node = self.head
		while(current_node):
			if(current_node in s):
				return True
			s.add(current_node)
			current_node = current_node.next
		return False

llist = LinkedList()
llist.insert('a')
llist.insert('b')
llist.insert('c')
llist.insert('d')
# llist.head.next.next.next.next = llist.head
llist.head.next.next.next.next = llist.head
if(llist.loop()):
	print("Ther is loop in linked list")
else:
	print("There is no loop in linked list")