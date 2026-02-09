MOD = 10**9 + 7

def main():
    import sys
    from collections import Counter
    input = sys.stdin.read
    data = input().split()
    
    N, K = int(data[0]), int(data[1])
    A = list(map(int, data[2:2+N]))
    
    freq = list(Counter(A).values())
    C = len(freq)
    
    if K >= C:
        result = 1
        for f in freq:
            result = (result * (f + 1)) % MOD
        print(result)
    else:
        dp = [0] * (K + 1)
        dp[0] = 1
        for f in freq:
            for j i