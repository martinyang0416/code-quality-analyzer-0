def main():
    import sys
    n, k = map(int, sys.stdin.readline().split())
    d = list(map(int, sys.stdin.readline().split()))
    
    # Compute prefix sums
    prefix = [0] * (n + 1)
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + d[i-1]
    
    def is_feasible(mask):
        # dp[i][j] means up to first i elements, j splits, meet the condition.
        dp = [[False]*(k+1) for _ in range(n+1)]
        dp[0][0] = True
        
        for i in range(1, n+1):
            for j 