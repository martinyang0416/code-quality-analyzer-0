import bisect

def smallestDistancePair(nums, k):
    nums.sort()
    n = len(nums)
    low, high = 0, nums[-1] - nums[0]
    
    while low < high:
        mid = (low + high) // 2
        count = 0
        for i in range(n):
            target = nums[i] + mid
            j = bisect.bisect_right(nums, target, i + 1, n)
            count += j - i - 1
        if count >= k:
            high = mid
        else:
            low = mid + 1
    return low