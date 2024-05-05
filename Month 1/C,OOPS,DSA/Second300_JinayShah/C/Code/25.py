def is_subset_sum(nums, target_sum):
    n = len(nums)
    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target_sum]

nums = [3, 34, 4, 12, 5, 2]
target_sum = 9

result = is_subset_sum(nums, target_sum)
print(f"Subset with sum {target_sum} {'exists' if result else 'does not exist'}.")