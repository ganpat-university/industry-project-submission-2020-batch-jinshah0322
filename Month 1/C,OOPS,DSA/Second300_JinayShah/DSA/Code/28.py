import random

class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.header = self.create_node(float('-inf'), max_level)
        self.level = 0

    def create_node(self, key, level):
        new_node = Node(key, level)
        return new_node

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, key):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        new_level = self.random_level()

        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.header
            self.level = new_level

        new_node = self.create_node(key, new_level)

        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, key):
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[0]

        if current and current.key == key:
            return True
        else:
            return False

    def display(self):
        for i in range(self.level + 1):
            node = self.header
            while node:
                print(node.key, end=" -> ")
                node = node.forward[i]
            print("")


skip_list = SkipList(max_level=3)
elements = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
for element in elements:
    skip_list.insert(element)

skip_list.display()


search_key = 19
result = skip_list.search(search_key)
print(f"Is {search_key} present in the skip list? {result}")
