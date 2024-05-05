class Node:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = {}

class AhoCorasick:
    def __init__(self, patterns):
        self.root = Node()
        self.build_tree(patterns)
        self.build_failure_function()

    def build_tree(self, patterns):
        for pattern in patterns:
            node = self.root
            for char in pattern:
                if char not in node.children:
                    node.children[char] = Node()
                node = node.children[char]
            node.output[pattern] = len(pattern)

    def build_failure_function(self):
        queue = []
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)
        while queue:
            node = queue.pop(0)
            for char, child in node.children.items():
                queue.append(child)
                fail_node = node.fail
                while fail_node and char not in fail_node.children:
                    fail_node = fail_node.fail
                child.fail = fail_node.children.get(char) if fail_node else self.root
                child.output.update(child.fail.output)

    def search(self, text):
        result = []
        node = self.root
        for i, char in enumerate(text):
            while node and char not in node.children:
                node = node.fail
            if node:
                node = node.children[char]
            for pattern, length in node.output.items():
                result.append((i - length + 1, i, pattern))
        return result

patterns = ["abc", "def"]
ac = AhoCorasick(patterns)

text = "abcdef"

matches = ac.search(text)
for match in matches:
    print(match)
