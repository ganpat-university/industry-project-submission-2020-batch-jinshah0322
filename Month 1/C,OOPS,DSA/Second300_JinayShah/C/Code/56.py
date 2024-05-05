import random

class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)

class SkipGraph:
    def __init__(self, max_level):
        self.max_level = max_level
        self.header = self.create_node(float('-inf'), max_level)

    def create_node(self, key, level):
        return Node(key, level)

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, key):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.max_level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        level = self.random_level()
        new_node = self.create_node(key, level)

        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, key):
        current = self.header

        for i in range(self.max_level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[0]

        if current and current.key == key:
            return True
        return False

skip_graph = SkipGraph(max_level=4)
keys = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
for key in keys:
    skip_graph.insert(key)

search_key = 17
result = skip_graph.search(search_key)
print(f"Key {search_key} found in Skip Graph: {result}")
