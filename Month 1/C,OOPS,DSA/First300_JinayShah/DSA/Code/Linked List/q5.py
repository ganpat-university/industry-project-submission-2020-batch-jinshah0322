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
	def intersection(self,llist1):
		s = set()
		currentNode1 = self.head
		currentNode2 = llist1.head
		while(currentNode1):
			s.add(currentNode1.data)
			currentNode1= currentNode1.next
		while(currentNode2):
			if(currentNode2.data in s):
				return currentNode2.data
			currentNode2=currentNode2.next
		return -1
		

llist = LinkedList()
llist.insert('a')
llist.insert('b')
llist.insert('c')
llist.insert('d')
llist1= LinkedList()
llist1.insert('d')
llist1.insert('e')
llist1.insert('f')
llist1.insert('g')
print(llist.intersection(llist1))