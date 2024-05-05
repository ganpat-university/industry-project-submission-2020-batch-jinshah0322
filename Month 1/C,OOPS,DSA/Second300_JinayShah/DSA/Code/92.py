import random

class SkipListNode:
    def __init__(self, key, value, level):
        self.key = key
        self.value = value
        self.forward = [None] * (level + 1)

class PersistentSkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.header = SkipListNode(float('-inf'), None, max_level)
        self.current_version = 0
    
    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, key, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.current_version, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        new_level = self.random_level()
        if new_level > self.current_version:
            self.current_version = new_level

        new_node = SkipListNode(key, value, new_level)

        for i in range(new_level + 1):
            if update[i] is not None:
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node
            else:
                self.header.forward[i] = new_node

    def search(self, key, version=None):
        current = self.header

        if version is None:
            version = self.current_version

        for i in range(version, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[0]
        if current and current.key == key:
            return current.value
        else:
            return None


skip_list = PersistentSkipList(max_level=4)


skip_list.insert(3, 'A')
skip_list.insert(6, 'B')
skip_list.insert(7, 'C')
skip_list.insert(9, 'D')
skip_list.insert(12, 'E')


print("Version 0:")
print("Key 6:", skip_list.search(6, version=0))  


skip_list.insert(1, 'F')
skip_list.insert(5, 'G')
skip_list.insert(10, 'H')


print("\nLatest Version:")
print("Key 6:", skip_list.search(6))  
print("Key 10:", skip_list.search(10))  
