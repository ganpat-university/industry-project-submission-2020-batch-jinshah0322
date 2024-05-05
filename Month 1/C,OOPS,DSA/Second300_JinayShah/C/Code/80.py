import concurrent.futures

def parallel_prefix_sum(data):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        prefix_sum = list(executor.map(lambda x: sum(data[:x]), range(1, len(data) + 1)))
    
    return prefix_sum

data = [1, 2, 3, 4, 5]
prefix_sum_result = parallel_prefix_sum(data)
print("Parallel Prefix Sum:", prefix_sum_result)