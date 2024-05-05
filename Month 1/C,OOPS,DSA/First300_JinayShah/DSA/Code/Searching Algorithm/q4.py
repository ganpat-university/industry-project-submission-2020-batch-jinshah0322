def search_rotated_array(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  

        # Check if the left half is sorted
        if arr[low] <= arr[mid]:
            # Check if the target is in the left half
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # The right half is sorted
            # Check if the target is in the right half
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1  # Element not found


rotated_array = [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
target_element = 7
result = search_rotated_array(rotated_array, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the rotated array.")