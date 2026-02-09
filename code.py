n, m = map(int, input().split())
matches = []
for _ in range(n):
    hi, mi, ni = map(int, input().split())
    matches.append((hi, mi, ni))

# Initialize DP table
dp = [ [-float('inf')] * (m + 1) for _ in range(n + 1) ]
dp[0][m] = 0  # Starting with m drinks, 0 matches played

for i in range(1, n + 1):
    hi, mi, ni = matches[i - 1]
    for k_prev in range(m + 1):
        if dp[i - 1][k_prev] != -float('inf'):
            # Option 1: Use high
            if k_prev >= 1:
                new_k =