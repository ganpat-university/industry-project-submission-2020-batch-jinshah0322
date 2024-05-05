import math

class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.hash_functions = hash_functions
        self.bit_array = [0] * size
        self.elements_count = 0

    def add(self, element):
        for i in range(self.hash_functions):
            index = hash((element, i)) % self.size
            self.bit_array[index] = 1

        self.elements_count += 1

    def contains(self, element):
        for i in range(self.hash_functions):
            index = hash((element, i)) % self.size
            if self.bit_array[index] == 0:
                return False

        return True

    def false_positive_probability(self):
        k = self.hash_functions
        n = self.elements_count
        m = self.size

        return (1 - math.exp(-k * n / m)) ** k

bloom_filter = BloomFilter(size=10, hash_functions=3)

elements_to_add = ["apple", "banana", "orange", "grape"]
for element in elements_to_add:
    bloom_filter.add(element)

element_to_check = "watermelon"
print(f"Does the Bloom filter contain {element_to_check}? {bloom_filter.contains(element_to_check)}")

false_positive_prob = bloom_filter.false_positive_probability()
print(f"False Positive Probability: {false_positive_prob}")
