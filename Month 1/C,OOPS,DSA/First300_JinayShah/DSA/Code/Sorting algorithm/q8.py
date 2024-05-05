def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of each digit at the current place value
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Modify count array to store cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)

    exp = 1
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


my_list = [904,46,5,74,62,1]
print("Original list:", my_list)
radix_sort(my_list)
print("Sorted list:", my_list)