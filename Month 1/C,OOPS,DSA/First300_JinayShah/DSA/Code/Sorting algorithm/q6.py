def heapify(arr, n, i):
    smallest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child

    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)  
    arr.reverse()


my_list = [4,6,10,9,2]
print("Original list:", my_list)
heap_sort(my_list)
print("Sorted list in ascending order:", my_list)