def lastStoneWeightII(stones):
    total = sum(stones)
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for stone in stones:
        for i in range(target, stone - 1, -1):
            if dp[i - stone]:
                dp[i] = True
    max_sum = 0
    for i in range(target, -1, -1):
        if dp[i]:
            max_sum = i
            break
    return total - 2 * max_sum