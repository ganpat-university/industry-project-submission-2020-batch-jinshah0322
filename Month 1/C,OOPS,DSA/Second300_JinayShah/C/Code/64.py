def jump(nums):
    if len(nums) <= 1:
        return 0

    max_reach, steps, last_jump_index = nums[0], 1, nums[0]

    for i in range(1, len(nums)):
        if i > max_reach:
            return -1  # Cannot reach this position

        if i > last_jump_index:
            steps += 1
            last_jump_index = max_reach

        max_reach = max(max_reach, i + nums[i])

    return steps

nums = [2, 3, 1, 1, 4]
result = jump(nums)
print(f"Minimum number of jumps: {result}")
