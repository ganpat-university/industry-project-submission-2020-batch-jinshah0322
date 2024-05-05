def can_partition_into_k_subsets(arr, K):
    total_sum = sum(arr)
    
    
    if total_sum % K != 0:
        return False
    
    target_sum = total_sum // K
    subset_sums = [0] * K
    
    def backtrack(index):
        if index == len(arr):
            return all(subset_sum == target_sum for subset_sum in subset_sums)
        
        for i in range(K):
            if subset_sums[i] + arr[index] <= target_sum:
                subset_sums[i] += arr[index]
                if backtrack(index + 1):
                    return True
                subset_sums[i] -= arr[index]
        
        return False
    
    return backtrack(0)


arr1 = [2, 1, 4, 5, 6]
K1 = 3
result1 = can_partition_into_k_subsets(arr1, K1)
print(f"For arr1, K1: {result1}")

arr2 = [2, 1, 5, 5, 6]
K2 = 3
result2 = can_partition_into_k_subsets(arr2, K2)
print(f"For arr2, K2: {result2}")
