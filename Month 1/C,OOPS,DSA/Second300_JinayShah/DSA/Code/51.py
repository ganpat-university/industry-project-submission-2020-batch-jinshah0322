import random

class SkipNode:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.header = SkipNode(float('-inf'), self.max_level)
        self.level = 0

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        new_level = self.random_level()

        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.header
            self.level = new_level

        new_node = SkipNode(value, new_level)

        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, value):
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]

        current = current.forward[0]

        if current and current.value == value:
            return True

        return False

    def display(self):
        for level in range(self.level + 1):
            node = self.header.forward[level]
            elements = []
            while node:
                elements.append(str(node.value))
                node = node.forward[level]
            print(f"Level {level}: {' -> '.join(elements)}")


skip_list = SkipList(max_level=3)

values_to_insert = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]
for value in values_to_insert:
    skip_list.insert(value)

print("Skip List after insertion:")
skip_list.display()

search_value = 19
if skip_list.search(search_value):
    print(f"{search_value} found in the skip list.")
else:
    print(f"{search_value} not found in the skip list.")
