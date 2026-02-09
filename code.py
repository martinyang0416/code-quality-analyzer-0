MOD = 10**9 + 7

def count_ways(s):
    n = len(s)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + (1 if s[i] == '1' else 0)
    
    total_ones = prefix[-1]
    if total_ones % 3 != 0:
        return 0
    
    if total_ones == 0:
        return ((n-1) * (n-2) // 2) % MOD
    
    target = total_ones // 3
    first_candidates = []
    for i in range(n):
        if prefix[i+1] == target:
            first_candidates.append(i)
    
    second_candidates = []
  