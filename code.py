T = int(input())
for _ in range(T):
    s = input().strip()
    n = len(s)
    if n == 0:
        print(0)
        continue
    dp = [[0] * n for _ in range(n)]
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1
            else:
                subtract = dp[i+1][j-1] if (i+1 <= j-1) else 0
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - subtract
    print(dp[0][n-1])