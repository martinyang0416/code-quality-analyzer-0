def canPartitionKSubsets(nums, k):
    total = sum(nums)
    if total % k != 0:
        return False
    target = total // k
    nums.sort(reverse=True)
    if nums and nums[0] > target:
        return False
    groups = [0] * k

    def backtrack(index):
        if index == len(nums):
            return True
        current = nums[index]
        for i in range(k):
            if i > 0 and groups[i] == groups[i-1]:
                continue
            if groups[i] + current <= target:
          