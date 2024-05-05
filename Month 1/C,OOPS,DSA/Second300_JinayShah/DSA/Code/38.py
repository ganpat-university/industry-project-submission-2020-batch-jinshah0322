class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1  
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index  

    def query(self, index):
        index += 1  
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index  
        return result


def fenwick_tree_example():
    array = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
    fenwick_tree = FenwickTree(len(array))

    
    for i, value in enumerate(array):
        fenwick_tree.update(i, value)

    
    print("Prefix Sum Queries:")
    for i in range(len(array)):
        prefix_sum = fenwick_tree.query(i)
        print(f"Prefix Sum of first {i+1} elements: {prefix_sum}")

    
    update_index = 2
    update_value = 2
    array[update_index] += update_value
    fenwick_tree.update(update_index, update_value)

    
    print("\nPrefix Sum Queries after Update:")
    for i in range(len(array)):
        prefix_sum = fenwick_tree.query(i)
        print(f"Prefix Sum of first {i+1} elements: {prefix_sum}")

fenwick_tree_example()
