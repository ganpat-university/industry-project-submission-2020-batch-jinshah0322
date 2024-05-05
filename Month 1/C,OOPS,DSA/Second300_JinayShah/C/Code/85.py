def countRangeSum(nums, lower, upper):
    def merge_sort_count(lo, hi):
        mid = (lo + hi) // 2
        if mid == lo:
            return 0
        count = merge_sort_count(lo, mid) + merge_sort_count(mid, hi)
        i = j = mid
        for left in prefix[lo:mid]:
            while i < hi and prefix[i] - left < lower:
                i += 1
            while j < hi and prefix[j] - left <= upper:
                j += 1
            count += j - i
        prefix[lo:hi] = sorted(prefix[lo:hi])
        return count

    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    return merge_sort_count(0, len(prefix))

nums = [-2, 5, -1]
lower, upper = -2, 2
result = countRangeSum(nums, lower, upper)
print("Count of Range Sum:", result)
