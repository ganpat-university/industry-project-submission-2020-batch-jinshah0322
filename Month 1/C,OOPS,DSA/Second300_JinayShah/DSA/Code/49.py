class CountingBloomFilter:
    def __init__(self, capacity, error_rate):
        self.capacity = capacity
        self.error_rate = error_rate
        self.size = self.calculate_size(capacity, error_rate)
        self.counters = [0] * self.size
        self.hash_functions = self.generate_hash_functions()

    @staticmethod
    def calculate_size(capacity, error_rate):
        return int(-capacity * math.log(error_rate) / (math.log(2) ** 2))

    def generate_hash_functions(self):
        hash_functions = []
        for seed in range(1, self.size + 1):
            hash_functions.append(self.create_hash_function(seed))
        return hash_functions

    def create_hash_function(self, seed):
        def hash_function(item):
            hash_val = seed
            for char in str(item):
                hash_val = (hash_val * 31) ^ ord(char)
            return hash_val % self.size

        return hash_function

    def add(self, item):
        for hash_function in self.hash_functions:
            index = hash_function(item)
            self.counters[index] += 1

    def check(self, item):
        for hash_function in self.hash_functions:
            index = hash_function(item)
            if self.counters[index] == 0:
                return False
        return True

    def remove(self, item):
        if not self.check(item):
            return

        for hash_function in self.hash_functions:
            index = hash_function(item)
            self.counters[index] -= 1


import math

def counting_bloom_filter_example():
    capacity = 1000
    error_rate = 0.01
    bloom_filter = CountingBloomFilter(capacity, error_rate)

    
    items_to_add = ["apple", "orange", "banana", "grape"]
    for item in items_to_add:
        bloom_filter.add(item)

    
    items_to_check = ["apple", "watermelon", "banana"]
    for item in items_to_check:
        if bloom_filter.check(item):
            print(f"{item} might be in the set.")
        else:
            print(f"{item} is definitely not in the set.")

counting_bloom_filter_example()
