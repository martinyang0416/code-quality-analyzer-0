n, k = map(int, input().split())
s = input().strip()
sorted_values = sorted(ord(c) - ord('a') + 1 for c in s)
INF = float('inf')
dp = [[INF] * (k + 1) for _ in range(n)]

for i in range(n):
    dp[i][1] = sorted_values[i]

for j in range(2, k + 1):
    for i in range(n):
        for prev in range(i):
            if sorted_values[i] - sorted_values[prev] >= 2:
                if dp[prev][j-1] + sorted_values[i] < dp[i][j]:
                    dp[i][j] = dp[prev][j-1] + sorted_values[i]

min_total