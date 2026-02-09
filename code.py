def checkSubarraySum(nums, k):
    if k == 0:
        # Check for two consecutive zeros
        for i in range(len(nums) - 1):
            if nums[i] == 0 and nums[i+1] == 0:
                return True
        return False
    else:
        k_abs = abs(k)
        mod_dict = {0: -1}  # To handle the case where subarray starts from index 0
        prefix_mod = 0
        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k_abs
            if prefix_mod in mod_dict:
      