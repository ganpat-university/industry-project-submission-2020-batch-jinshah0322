import heapq

def burstsort(data, block_size):    
    sorted_blocks = []
    for i in range(0, len(data), block_size):
        block = data[i:i + block_size]
        block.sort()
        sorted_blocks.append(block)

    
    result = []
    heap = [(block[0], block, i, 0) for i, block in enumerate(sorted_blocks) if block]
    heapq.heapify(heap)

    while heap:
        _, block, block_index, index = heapq.heappop(heap)
        result.append(block[index])

        index += 1
        if index < len(block):
            heapq.heappush(heap, (block[index], block, block_index, index))

    return result


input_data = [4, 2, 7, 1, 9, 5, 3, 8, 6]
block_size = 3

sorted_data = burstsort(input_data, block_size)
print(sorted_data)
