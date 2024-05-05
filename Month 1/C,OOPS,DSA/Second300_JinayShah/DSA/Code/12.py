def min_operations_for_pairing(N, arr):
    even_count = sum(1 for num in arr if num % 2 == 0)
    odd_count = N - even_count
    
    return abs(even_count - odd_count) // 2


N1 = 2
arr1 = [3, 0, 2, 1]
result1 = min_operations_for_pairing(N1, arr1)
print(f"Minimum operations for Example 1: {result1}")


N2 = 3
arr2 = [1, 0, 3, 2, 4, 5]
result2 = min_operations_for_pairing(N2, arr2)
print(f"Minimum operations for Example 2: {result2}")
