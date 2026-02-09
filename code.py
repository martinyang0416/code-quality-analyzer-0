from collections import defaultdict

def subarraySum(nums, k):
    count = 0
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    current_sum = 0
    for num in nums:
        current_sum += num
        count += prefix_sum.get(current_sum - k, 0)
        prefix_sum[current_sum] += 1
    return count