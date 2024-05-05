def fractional_cascading(arrays):
    n = len(arrays)
    indices = [0] * n  

    def find_in_array(arr, value):
        low, high = 0, len(arr)

        while low < high:
            mid = (low + high) // 2
            if arr[mid] < value:
                low = mid + 1
            else:
                high = mid

        return low

    def search(value):
        positions = []

        for i in range(n):
            pos = find_in_array(arrays[i], value)
            positions.append(pos)

            if pos < len(arrays[i]) and arrays[i][pos] == value:
                
                pos += 1

            indices[i] = pos  

        return positions

    
    search_result = search(5)
    print("Positions of 5 in each array:", search_result)


sorted_arrays = [
    [1, 3, 5, 7, 9],
    [2, 4, 6, 8, 10],
    [5, 10, 15, 20, 25]
]

fractional_cascading(sorted_arrays)
