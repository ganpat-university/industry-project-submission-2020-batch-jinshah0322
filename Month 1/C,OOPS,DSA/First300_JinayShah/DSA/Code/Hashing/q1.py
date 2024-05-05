class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None  

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        previous = None

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                return True  
            previous = current
            current = current.next

        return False  


my_hash_table = HashTable(size=10)

my_hash_table.insert("apple", 5)
my_hash_table.insert("banana", 8)
my_hash_table.insert("cherry", 12)

print("Search 'apple':", my_hash_table.search("apple"))  
print("Search 'orange':", my_hash_table.search("orange"))  

print("Deleting 'banana'...")
deleted = my_hash_table.delete("banana")
if deleted:
    print("Search 'banana':", my_hash_table.search("banana"))  
else:
    print("'banana' not found.")

print("Search 'cherry':", my_hash_table.search("cherry"))  