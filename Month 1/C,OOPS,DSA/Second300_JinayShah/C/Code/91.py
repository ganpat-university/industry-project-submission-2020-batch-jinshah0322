import math
import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, initial_capacity, false_positive_rate):
        self.capacity = initial_capacity
        self.false_positive_rate = false_positive_rate
        self.size = self.calculate_size(initial_capacity, false_positive_rate)
        self.hash_functions = self.calculate_hash_functions(initial_capacity, self.size)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)
        self.elements_count = 0

    def calculate_size(self, capacity, false_positive_rate):
        return int(-(capacity * math.log(false_positive_rate)) / (math.log(2) ** 2))

    def calculate_hash_functions(self, capacity, size):
        num_hashes = int((size / capacity) * math.log(2))
        return [lambda x, i=i: mmh3.hash(str(x), i) % size for i in range(num_hashes)]

    def add(self, element):
        for hash_function in self.hash_functions:
            index = hash_function(element)
            self.bit_array[index] = 1
        self.elements_count += 1

        # Check if resizing is needed
        if self.elements_count > self.capacity * self.false_positive_rate:
            self.resize()

    def contains(self, element):
        for hash_function in self.hash_functions:
            index = hash_function(element)
            if not self.bit_array[index]:
                return False
        return True

    def resize(self):
        new_capacity = self.capacity * 2
        new_size = self.calculate_size(new_capacity, self.false_positive_rate)
        new_hash_functions = self.calculate_hash_functions(new_capacity, new_size)

        new_bit_array = bitarray(new_size)
        new_bit_array.setall(0)

        # Transfer existing elements to the new array
        for i in range(len(self.bit_array)):
            if self.bit_array[i]:
                for hash_function in new_hash_functions:
                    index = hash_function(i)
                    new_bit_array[index] = 1

        # Update the filter parameters
        self.capacity = new_capacity
        self.size = new_size
        self.hash_functions = new_hash_functions
        self.bit_array = new_bit_array

# Example usage:
initial_capacity = 100
false_positive_rate = 0.01
bloom_filter = BloomFilter(initial_capacity, false_positive_rate)

# Add elements to the Bloom filter
elements_to_add = ["apple", "banana", "orange", "grape"]
for element in elements_to_add:
    bloom_filter.add(element)

# Check if an element is in the Bloom filter
element_to_check = "apple"
print(f"Does the Bloom filter contain {element_to_check}? {bloom_filter.contains(element_to_check)}")

# Resize the Bloom filter
bloom_filter.resize()

# Check if an element is in the Bloom filter after resizing
print(f"Does the Bloom filter contain {element_to_check} after resizing? {bloom_filter.contains(element_to_check)}")
