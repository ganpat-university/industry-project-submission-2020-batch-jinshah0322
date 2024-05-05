from collections import defaultdict
import mmh3

class CountMinSketch:
    def __init__(self, width, depth):
        self.width = width
        self.depth = depth
        self.count_matrix = [[0] * width for _ in range(depth)]
        self.hash_functions = [lambda x, i=i: mmh3.hash(str(x) + str(i)) % width for i in range(depth)]

    def update(self, key, value):
        for i, hash_func in enumerate(self.hash_functions):
            col = hash_func(key)
            self.count_matrix[i][col] += value

    def query(self, key):
        return min(self.count_matrix[i][hash_func(key)] for i, hash_func in enumerate(self.hash_functions))

# Example Usage:
count_min_sketch = CountMinSketch(width=5, depth=3)

data = [("apple", 3), ("banana", 5), ("orange", 2)]
for key, value in data:
    count_min_sketch.update(key, value)

query_key = "apple"
query_result = count_min_sketch.query(query_key)
print(f"Estimated count for '{query_key}': {query_result}")
