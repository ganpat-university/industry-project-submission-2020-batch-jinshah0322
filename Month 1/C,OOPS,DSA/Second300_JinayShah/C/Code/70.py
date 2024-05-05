from collections import Counter

def findShortestSubarray(nums):
    count = Counter(nums)
    max_freq = max(count.values())
    elements = [key for key, value in count.items() if value == max_freq]

    first_occurrence = {}
    last_occurrence = {}

    for i, num in enumerate(nums):
        if num not in first_occurrence:
            first_occurrence[num] = i
        last_occurrence[num] = i

    min_length = float('inf')

    for num in elements:
        min_length = min(min_length, last_occurrence[num] - first_occurrence[num] + 1)

    return min_length

nums = [1, 2, 2, 3, 1]
result = findShortestSubarray(nums)
print(f"Minimum length of a subarray with the same degree: {result}")
