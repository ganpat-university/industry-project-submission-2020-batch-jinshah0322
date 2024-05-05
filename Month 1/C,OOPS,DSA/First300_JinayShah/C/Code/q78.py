class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value
        raise KeyError(f"Key '{key}' not found.")

    def delete(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    return
        raise KeyError(f"Key '{key}' not found.")

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")

hash_table = HashTable()

hash_table.insert("one", 1)
hash_table.insert("two", 2)
hash_table.insert("three", 3)

print("Hash Table:")
hash_table.display()

print("Get value for key 'two':", hash_table.get("two"))

hash_table.delete("two")

print("Hash Table after deleting key 'two':")
hash_table.display()