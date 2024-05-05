class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.middle = None
        self.right = None
        self.value = None  

class TernarySearchTree:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self._put(self.root, key, value, 0)

    def _put(self, node, key, value, depth):
        char = key[depth]

        if node is None:
            node = TSTNode(char)

        if char < node.char:
            node.left = self._put(node.left, key, value, depth)
        elif char > node.char:
            node.right = self._put(node.right, key, value, depth)
        elif depth < len(key) - 1:
            node.middle = self._put(node.middle, key, value, depth + 1)
        else:
            node.value = value

        return node

    def get(self, key):
        node = self._get(self.root, key, 0)
        return node.value if node else None

    def _get(self, node, key, depth):
        if node is None:
            return None

        char = key[depth]

        if char < node.char:
            return self._get(node.left, key, depth)
        elif char > node.char:
            return self._get(node.right, key, depth)
        elif depth < len(key) - 1:
            return self._get(node.middle, key, depth + 1)
        else:
            return node


tst = TernarySearchTree()

tst.put("apple", 42)
tst.put("orange", 25)
tst.put("banana", 10)

print("Value for 'apple':", tst.get("apple"))    
print("Value for 'orange':", tst.get("orange"))  
print("Value for 'banana':", tst.get("banana"))  
print("Value for 'grape':", tst.get("grape"))    
