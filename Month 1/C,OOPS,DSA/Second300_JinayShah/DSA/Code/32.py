class TrieNode:
    def __init__(self):
        self.children = {}
        self.failure_link = None
        self.output = []

class AhoCorasick:
    def __init__(self):
        self.root = TrieNode()

    def add_pattern(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.output.append(pattern)

    def build_failure_links(self):
        queue = []

        for child in self.root.children.values():
            child.failure_link = self.root
            queue.append(child)

        while queue:
            current_node = queue.pop(0)

            for char, child in current_node.children.items():
                queue.append(child)
                failure_link_node = current_node.failure_link

                while failure_link_node and char not in failure_link_node.children:
                    failure_link_node = failure_link_node.failure_link

                if failure_link_node:
                    child.failure_link = failure_link_node.children[char]
                else:
                    child.failure_link = self.root

                child.output += child.failure_link.output

    def search(self, text):
        current_node = self.root
        matches = []

        for i, char in enumerate(text):
            while current_node and char not in current_node.children:
                current_node = current_node.failure_link

            if current_node:
                current_node = current_node.children.get(char, self.root)
                matches.extend(current_node.output)

        return matches


def aho_corasick_example():
    ac = AhoCorasick()

    patterns = ["he", "she", "his", "hers"]
    text = "ushers"

    for pattern in patterns:
        ac.add_pattern(pattern)

    ac.build_failure_links()
    result = ac.search(text)

    print(f"Text: {text}")
    print(f"Matches: {result}")

aho_corasick_example()
