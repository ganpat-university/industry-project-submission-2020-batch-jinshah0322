class SparseTable:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.log_table = [0] * (self.n + 1)
        self.build_sparse_table()

    def build_sparse_table(self):
        for i in range(2, self.n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1

        k_max = self.log_table[self.n]
        self.table = [[0] * k_max for _ in range(self.n)]

        for i in range(self.n):
            self.table[i][0] = i

        for j in range(1, k_max):
            for i in range(self.n - (1 << j) + 1):
                left = self.table[i][j - 1]
                right = self.table[i + (1 << (j - 1))][j - 1]

                self.table[i][j] = left if self.arr[left] <= self.arr[right] else right

    def query(self, left, right):
        k = self.log_table[right - left + 1]
        left_max = self.table[left][k]
        right_max = self.table[right - (1 << k) + 1][k]
        return min(left_max, right_max)


arr = [2, 6, 4, 1, 8, 3, 5, 7]
sparse_table = SparseTable(arr)


result = sparse_table.query(2, 5)
print("Minimum in range [2, 5]:", arr[result])


result = sparse_table.query(1, 6)
print("Minimum in range [1, 6]:", arr[result])
