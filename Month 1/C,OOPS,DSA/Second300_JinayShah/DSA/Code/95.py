import math

class SqrtDecomposition:
    def __init__(self, arr):
        self.arr = arr
        self.size = int(math.ceil(math.sqrt(len(arr))))
        self.blocks = [0] * self.size

        for i in range(len(arr)):
            self.blocks[i // self.size] += arr[i]

    def update_range(self, start, end, value):
        block_start = start // self.size
        block_end = end // self.size

        for i in range(block_start, block_end + 1):
            if start <= i * self.size and end >= (i + 1) *  self.size - 1:
                
                self.blocks[i] += value * self.size
            else:
                
                for j in range(max(start, i * self.size), min(end, (i + 1) * self.size)):
                    self.arr[j] += value
                    self.blocks[i] += value

    def query_range(self, start, end):
        block_start = start // self.size
        block_end = end // self.size
        result = 0

        for i in range(block_start, block_end + 1):
            if start <= i * self.size and end >= (i + 1) * self.size - 1:
                
                result += self.blocks[i]
            else:
                
                result += sum(self.arr[j] for j in range(max(start, i * self.size), min(end, (i + 1) * self.size)))

        return result


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sqrt_decomp = SqrtDecomposition(arr)


print(sqrt_decomp.query_range(2, 6))  


sqrt_decomp.update_range(3, 7, 2)


print(sqrt_decomp.query_range(2, 6))  