def max_subarray_sum_circular(nums):
    def kadane(nums):
        max_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

    total_sum = sum(nums)
    max_non_circular = kadane(nums)
    max_circular = total_sum + kadane([-num for num in nums[1:-1]])
    return max(max_non_circular, max_circular) if max_circular != 0 else max_non_circular

nums = [1, -2, 3, -2]
result = max_subarray_sum_circular(nums)
print(f"Maximum subarray sum (circular): {result}")
