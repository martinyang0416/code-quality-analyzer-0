def main():
    import sys
    s = sys.stdin.read().strip()
    target = 'bessie'
    m = len(target)  # 6
    n = len(s)
    
    dp = [0] * (m + 1)
    dp[0] = 1  # Base case: empty string matches the first 0 characters
    
    total = 0
    
    for c in s:
        new_dp = dp.copy()
        for i in range(m, 0, -1):
            if c == target[i-1]:
                new_dp[i] += new_dp[i-1]
        dp = new_dp
        total += dp[m]
    
    print(total)

if __name__ == "__main__":
    main()