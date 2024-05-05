class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [False] * size

    def _hash(self, element, seed):
        hash_value = 0
        for char in element:
            hash_value = (hash_value * seed + ord(char)) % self.size
        return hash_value

    def add(self, element):
        for seed in range(1, self.num_hashes + 1):
            index = self._hash(element, seed) % self.size
            self.bit_array[index] = True

    def contains(self, element):
        for seed in range(1, self.num_hashes + 1):
            index = self._hash(element, seed) % self.size
            if not self.bit_array[index]:
                return False
        return True


bloom_filter = BloomFilter(size=10, num_hashes=3)


elements_to_add = ["apple", "banana", "orange"]
for element in elements_to_add:
    bloom_filter.add(element)


print(bloom_filter.contains("apple"))    
print(bloom_filter.contains("grape"))    
