class SuffixNode:
    def __init__(self):
        self.children = {}


def build_suffix_tree(text):
    root = SuffixNode()
    for i in range(len(text)):
        current = root
        for j in range(i, len(text)):
            if text[j] not in current.children:
                current.children[text[j]] = SuffixNode()
            current = current.children[text[j]]
    return root


text = "banana"
root = build_suffix_tree(text)