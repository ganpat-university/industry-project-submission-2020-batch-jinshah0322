import concurrent.futures

def parallel_binary_search(arr, target):
    def binary_search(segment):
        low, high = segment
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1  

    num_processors = min(len(arr), 4)  
    segment_size = len(arr) // num_processors

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_processors) as executor:
        segments = [(i * segment_size, (i + 1)*  segment_size - 1) for i in range(num_processors - 1)]
        segments.append(((num_processors - 1) * segment_size, len(arr) - 1))

        futures = [executor.submit(binary_search, segment) for segment in segments]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result != -1:
                return result 

    return -1 

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7
result = parallel_binary_search(sorted_array, target_value)
print(f"Index of {target_value}: {result}")