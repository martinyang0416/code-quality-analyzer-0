def main():
    import sys
    height = int(sys.stdin.readline().strip())
    N = int(sys.stdin.readline().strip())
    steps = list(map(int, sys.stdin.readline().strip().split()))
    dp = [0] * (height + 1)
    dp[0] = 1  # base case: one way to reach 0
    
    for i in range(1, height + 1):
        for s in steps:
            if i >= s:
                dp[i] += dp[i - s]
    print(dp[height])

if __name__ == "__main__":
    main()