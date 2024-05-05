def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    n = len(nums)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)

arr = [10, 22, 9, 33, 21, 50, 41, 60]
result = longest_increasing_subsequence(arr)
print("Length of the Longest Increasing Subsequence:", result)
