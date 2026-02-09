def longestSubsequence(arr, difference):
    dp = {}
    max_len = 0
    for num in arr:
        prev = num - difference
        current_length = dp.get(prev, 0) + 1
        dp[num] = current_length
        if current_length > max_len:
            max_len = current_length
    return max_len