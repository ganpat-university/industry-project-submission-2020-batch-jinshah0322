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

    def get_all_words(self):
        words = []
        self._collect_words(self.root, "", words)
        return words

    def _collect_words(self, node, current_word, words):
        if node.is_end_of_word:
            words.append(current_word)

        for char, child_node in node.children.items():
            self._collect_words(child_node, current_word + char, words)

def isAnagram(dict_word, word):
    if sorted(word)== sorted(dict_word):
        return True
    else:
        return False

trie = Trie()
user_word = "leap"

words = ["apple", "peal", "app", "apricot", "banana", "bat"]
for word in words:
    trie.insert(word)


words_back = trie.get_all_words()

for word in words_back:
    if isAnagram(word, user_word):
        print(word, "is anagram to", user_word)