class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1  
def build_suffix_trie(text):
    root = TrieNode()

    for i in range(len(text)):
        current_node = root
        suffix = text[i:]

        for char in suffix:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.index = i 

    return root

def traverse_suffix_trie(node, suffix_array):
    if node.index != -1:
        suffix_array.append(node.index)

    for char, child_node in node.children.items():
        traverse_suffix_trie(child_node, suffix_array)

def build_suffix_array(text):
    suffix_trie = build_suffix_trie(text)
    suffix_array = []
    traverse_suffix_trie(suffix_trie, suffix_array)
    return suffix_array

text = "banana"
suffix_array_result = build_suffix_array(text)

print("Text:", text)
print("Suffix Array:", suffix_array_result)
