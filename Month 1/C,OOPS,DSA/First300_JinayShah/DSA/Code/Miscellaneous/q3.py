def find_majority_element(nums):
    element_count = {}

    for num in nums:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    majority_element = None
    max_count = 0

    for key, value in element_count.items():
        if value > max_count:
            max_count = value
            majority_element = key

    if max_count > len(nums) // 2:
        return majority_element
    else:
        return None  


input_array = [3, 3, 4, 2, 4, 4, 2, 4, 4]
majority_element = find_majority_element(input_array)
if majority_element is not None:
    print(f"The majority element is: {majority_element}")
else:
    print("No majority element found.")