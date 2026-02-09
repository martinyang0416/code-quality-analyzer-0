import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    
    max_a = int(N ** 0.5)
    squares = [a * a for a in range(0, max_a + 1)]
    
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = True
    
    for i in range(1, N + 1):
        for k in range(1, M + 1):
            for s in squares:
                if s > i:
                    continue
                prev_i = i - s
                prev_k = k - 1
                if prev_k >= 0 and dp[prev_i][prev_k