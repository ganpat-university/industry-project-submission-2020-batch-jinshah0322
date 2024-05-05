import ctypes
class Node:
	def __init__(self, data):
		
		self.data = data
		self.npx = 0

class XorLinkedList:
	def __init__(self):		
		self.head = None
		self.__nodes = []
		
	
	def XOR(self, a, b):		
		return a ^ b	

	def insert(self, data):
		node = Node(data)
		node.npx = id(self.head)

		if self.head is not None:
			self.head.npx = self.XOR(id(node), 
									self.head.npx)

		self.__nodes.append(node)
		self.head = node
	def printList(self):
	
		if self.head != None:
			prev_id = 0
			curr = self.head
			next_id = 1
			print("Following are the nodes of Linked List:")
			
			while curr is not None:
				print(curr.data, end = ' ')
				next_id = self.XOR(prev_id, curr.npx)
				prev_id = id(curr)
				curr = self.__type_cast(next_id)
	def __type_cast(self, id):
		return ctypes.cast(id, ctypes.py_object).value


if __name__ == '__main__':
	
	obj = XorLinkedList()
	obj.insert(10)
	obj.insert(20)
	obj.insert(30)
	obj.insert(40)
	obj.printList()


