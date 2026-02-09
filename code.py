def maxProduct(nums):
    if not nums:
        return 0
    current_max = current_min = result = nums[0]
    for num in nums[1:]:
        temp_max = max(num, current_max * num, current_min * num)
        temp_min = min(num, current_max * num, current_min * num)
        current_max, current_min = temp_max, temp_min
        result = max(result, current_max)
    return result