def minCost(houses, cost, m, n, target):
    INF = float('inf')
    # Initialize DP table with infinity
    dp = [[[INF] * (n + 1) for _ in range(target + 1)] for __ in range(m)]
    
    # Base case: first house
    if houses[0] == 0:
        for c in range(1, n + 1):
            dp[0][1][c] = cost[0][c - 1]
    else:
        dp[0][1][houses[0]] = 0
    
    # Fill DP table
    for i in range(1, m):
        for k_prev in range(1, target + 1):
            for c_prev in range(1, n + 1):
         