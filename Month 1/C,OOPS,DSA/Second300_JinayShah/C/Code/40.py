import heapq 

class Node: 
	def __init__(self, freq, symbol, left=None, right=None): 
		self.freq = freq 
		self.symbol = symbol 
		self.left = left 
		self.right = right 
		self.huff = '' 

	def __lt__(self, nxt): 
		return self.freq < nxt.freq 


def printNodes(node, val=''): 

	newVal = val + str(node.huff) 

	if(node.left): 
		printNodes(node.left, newVal) 
		
	if(node.right): 
		printNodes(node.right, newVal) 

	if(not node.left and not node.right): 
		print(f"{node.symbol} : {newVal}") 

text = input("Enter text:")
mydict = {}

for char in text.lower():
	if char==' ':
		continue
	elif char in mydict.keys():
		mydict[char] += 1
	else:
		mydict[char] = 1

chars = list(mydict.keys())
freq = list(mydict.values())
nodes = [] 

for x in range(len(chars)): 
	heapq.heappush(nodes, Node(freq[x], chars[x])) 
	
while len(nodes) > 1: 

	left = heapq.heappop(nodes) 
	right = heapq.heappop(nodes) 

	left.huff = 0
	right.huff = 1

	newNode = Node(left.freq+right.freq, left.symbol+right.symbol, left, right) 

	heapq.heappush(nodes, newNode) 

printNodes(nodes[0]) 