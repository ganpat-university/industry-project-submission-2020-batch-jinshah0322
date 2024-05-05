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

class SpellChecker:
    def __init__(self, dictionary):
        self.trie = Trie()
        for word in dictionary:
            self.trie.insert(word.lower())  
    def check_spelling(self, word):
        return self.trie.search(word.lower())

dictionary = ["apple", "banana", "orange", "grape", "pear", "peach"]
spell_checker = SpellChecker(dictionary)

words_to_check = ["apple", "orange", "kiwi", "Banana", "peachy"]
for word in words_to_check:
    if spell_checker.check_spelling(word):
        print(f"{word} is spelled correctly.")
    else:
        print(f"{word} is misspelled.")
