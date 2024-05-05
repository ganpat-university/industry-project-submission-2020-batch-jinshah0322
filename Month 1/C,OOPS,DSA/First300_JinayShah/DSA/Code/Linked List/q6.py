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
	def remveDuplicate(self):
		list = set()
		currentNode = self.head
		list.add(currentNode.data)
		while(currentNode.next):
			if(currentNode.next.data in list):
				temp = currentNode.next
				currentNode.next = temp.next
				temp = None
			else:
				list.add(currentNode.next.data)
				currentNode = currentNode.next

llist = LinkedList()
llist.insert('a')
llist.insert('b')
llist.insert('c')
llist.insert('d')
llist.insert('a')
llist.traverse()
print()
print("Printing after removing duplicate elements")
llist.remveDuplicate()
llist.traverse()