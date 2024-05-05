class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

trie = Trie()

words_to_insert = ["apple", "app", "apricot", "banana", "bat", "batman", "batter"]
for word in words_to_insert:
    trie.insert(word)

words_to_search = ["apple", "app", "apricot", "banana", "bat", "batter", "batman", "batwoman"]
for word in words_to_search:
    if trie.search(word):
        print(f"{word} is in the Trie.")
    else:
        print(f"{word} is not in the Trie.")