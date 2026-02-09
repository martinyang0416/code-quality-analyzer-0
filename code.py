n = int(input())
s = list(map(int, input().split()))
max_dp = {}
max_sum = 0

for i in range(n):
    k = s[i] - (i + 1)
    if k in max_dp:
        current = max_dp[k] + s[i]
    else:
        current = s[i]
    if k in max_dp:
        if current > max_dp[k]:
            max_dp[k] = current
    else:
        max_dp[k] = current
    if current > max_sum:
        max_sum = current

print(max_sum)