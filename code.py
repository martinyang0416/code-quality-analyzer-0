def mergeStones(stones, K):
    n = len(stones)
    if (n - 1) % (K - 1) != 0:
        return -1
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + stones[i]
    
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            total = prefix[j + 1] - prefix[i]
            for k in range(i, j):
                left_len = k 