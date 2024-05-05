class RadixTreeNode:
   def __init__(self, value=None):
       self.value = value
       self.children = {}
       self.is_end = False

class RadixTree:
   def __init__(self):
       self.root = RadixTreeNode()

   def insert(self, key, value):
       node = self.root

       for char in key:
           if char not in node.children:
               node.children[char] = RadixTreeNode()
           node = node.children[char]
       
       node.is_end = True
       node.value = value

   def search(self, key):
       node = self.root

       for char in key:
           if char not in node.children:
               return None
           node = node.children[char]

       return node.value if node.is_end else None

radix_tree = RadixTree()

radix_tree.insert("hello", "world")
radix_tree.insert("water", "flow")
radix_tree.insert("cloud", "rain")

print("hello ->", radix_tree.search("hello"))   # Output: world
print("other ->", radix_tree.search("other"))   # Output: None