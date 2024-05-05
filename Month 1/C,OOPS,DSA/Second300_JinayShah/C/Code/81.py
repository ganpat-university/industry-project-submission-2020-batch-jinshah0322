def countSubarraysWithSum(nums, target):
    prefix_sum = {0: 1}  
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        if current_sum - target in prefix_sum:
            count += prefix_sum[current_sum - target]

        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

    return count

nums = [1, 0, 1, 0, 1]
target_sum = 2
result = countSubarraysWithSum(nums, target_sum)
print("Count of Subarrays with Given Sum:", result)
