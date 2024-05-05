from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return [key for key, _ in count.most_common(k)]

nums = [1, 1, 1, 2, 2, 3]
k = 2
result = topKFrequent(nums, k)
print(f"Top {k} frequent elements:", result)
