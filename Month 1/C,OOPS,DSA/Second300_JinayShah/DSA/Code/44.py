import random

class SkipGraphNode:
    def __init__(self, key, height):
        self.key = key
        self.forward = [None] * (height + 1)

class SkipGraph:
    def __init__(self, max_height):
        self.max_height = max_height
        self.header = SkipGraphNode(None, max_height)
        self.current_height = 0

    def random_height(self):
        height = 1
        while random.random() < 0.5 and height < self.max_height:
            height += 1
        return height

    def insert(self, key):
        update = [None] * (self.max_height + 1)
        current = self.header

        for i in range(self.current_height, 0, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        new_height = self.random_height()
        if new_height > self.current_height:
            for i in range(self.current_height + 1, new_height + 1):
                update[i] = self.header
            self.current_height = new_height

        new_node = SkipGraphNode(key, new_height)

        for i in range(1, new_height + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, key):
        current = self.header
        for i in range(self.current_height, 0, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[1]
        if current and current.key == key:
            return True
        return False

    def delete(self, key):
        update = [None] * (self.max_height + 1)
        current = self.header

        for i in range(self.current_height, 0, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[1]

        if current and current.key == key:
            for i in range(1, self.current_height + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.current_height > 1 and not self.header.forward[self.current_height]:
                self.current_height -= 1

    def display(self):
        for level in range(self.current_height, 0, -1):
            current = self.header
            while current.forward[level]:
                print(current.forward[level].key, end=" ")
                current = current.forward[level]
            print()


def skip_graph_example():
    skip_graph = SkipGraph(max_height=4)

    keys_to_insert = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25, 29]
    for key in keys_to_insert:
        skip_graph.insert(key)

    print("Skip graph after insertion:")
    skip_graph.display()

    key_to_search = 17
    result = skip_graph.search(key_to_search)
    print(f"Search result for key {key_to_search}: {result}")

    key_to_delete = 12
    skip_graph.delete(key_to_delete)
    print(f"Skip graph after deletion of key {key_to_delete}:")
    skip_graph.display()

skip_graph_example()
