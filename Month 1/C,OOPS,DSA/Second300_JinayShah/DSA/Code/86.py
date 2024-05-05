class TrieNode:
    def __init__(self, key=None):
        self.key = key
        self.children = {}
        self.is_end_of_word = False

class BinaryTreeNode:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

class TwoLevelTree:
    def __init__(self):
        self.trie_root = TrieNode()
        self.bst_root = None

    def insert(self, key):
        self._insert_trie(key)
        self._insert_bst(key)

    def _insert_trie(self, key):
        trie_node = self.trie_root

        for char in key:
            if char not in trie_node.children:
                trie_node.children[char] = TrieNode(char)
            trie_node = trie_node.children[char]

        trie_node.is_end_of_word = True

    def _insert_bst(self, key):
        if not self.bst_root:
            self.bst_root = BinaryTreeNode(key)
        else:
            self._insert_bst_recursive(self.bst_root, key)

    def _insert_bst_recursive(self, node, key):
        if key < node.key:
            if node.left:
                self._insert_bst_recursive(node.left, key)
            else:
                node.left = BinaryTreeNode(key)
        elif key > node.key:
            if node.right:
                self._insert_bst_recursive(node.right, key)
            else:
                node.right = BinaryTreeNode(key)

    def search(self, key):
        return self._search_trie(key) and self._search_bst(key)

    def _search_trie(self, key):
        trie_node = self.trie_root

        for char in key:
            if char not in trie_node.children:
                return False
            trie_node = trie_node.children[char]

        return trie_node.is_end_of_word

    def _search_bst(self, key):
        return self._search_bst_recursive(self.bst_root, key)

    def _search_bst_recursive(self, node, key):
        if not node:
            return False

        if key == node.key:
            return True
        elif key < node.key:
            return self._search_bst_recursive(node.left, key)
        else:
            return self._search_bst_recursive(node.right, key)


two_level_tree = TwoLevelTree()

keys = ["apple", "app", "banana", "bat", "batman", "batwoman"]
for key in keys:
    two_level_tree.insert(key)

search_result = two_level_tree.search("bat")
print(search_result)  

search_result = two_level_tree.search("batwoman")
print(search_result)  

search_result = two_level_tree.search("orange")
print(search_result)  
