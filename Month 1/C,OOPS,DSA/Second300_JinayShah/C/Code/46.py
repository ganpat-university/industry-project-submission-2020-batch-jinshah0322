def subset_sum(nums, target):
    def backtrack(i, current_sum):
        if current_sum == target:
            return True
        if i >= len(nums) or current_sum > target:
            return False
        if backtrack(i + 1, current_sum + nums[i]):
            return True
        return backtrack(i + 1, current_sum)
    return backtrack(0, 0)

nums = [3, 2, 7, 1]
target = 6
if subset_sum(nums, target):
    print("A subset with the given sum exists.")
else:
    print("No subset with the given sum exists.")