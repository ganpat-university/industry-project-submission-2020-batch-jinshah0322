class SegmentTree:
    def __init__(self, arr):
        self.size = len(arr)
        self.tree = [float('inf')] * (2 ** (self.size.bit_length()+1)-1)
        self.construct_tree(arr, 0, self.size - 1, 0)

    def construct_tree(self, arr, start, end, index):
        if start == end:
            self.tree[index] = arr[start]
            return

        mid = (start + end) // 2
        self.construct_tree(arr, start, mid, 2 * index + 1)
        self.construct_tree(arr, mid + 1, end, 2 * index + 2)
        self.tree[index] = min(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def update(self, arr_index, new_value, start=0, end=None, index=0):
        if end is None:
            end = self.size - 1

        if start == end:
            self.tree[index] = new_value
            return

        mid = (start + end) // 2
        if arr_index <= mid:
            self.update(arr_index, new_value, start, mid, 2 * index + 1)
        else:
            self.update(arr_index, new_value, mid + 1, end, 2 * index + 2)

        self.tree[index] = min(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def query(self, query_start, query_end, start=0, end=None, index=0):
        if end is None:
            end = self.size - 1

        
        if query_start > end or query_end < start:
            return float('inf')

        
        if query_start <= start and query_end >= end:
            return self.tree[index]

        
        mid = (start + end) // 2
        left_min = self.query(query_start, query_end, start, mid, 2 * index + 1)
        right_min = self.query(query_start, query_end, mid + 1, end, 2 * index + 2)

        return min(left_min, right_min)


arr = [1, 3, 2, 7, 9, 11]
segment_tree = SegmentTree(arr)


print(segment_tree.query(1, 4))  


segment_tree.update(2, 5)


print(segment_tree.query(1, 4))  