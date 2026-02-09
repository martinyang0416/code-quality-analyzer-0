MOD = 10**9 + 7

def numberWays(hats):
    n = len(hats)
    from collections import defaultdict
    hat_to_people = defaultdict(list)
    for p in range(n):
        for h in hats[p]:
            hat_to_people[h].append(p)
    
    dp = [0] * (1 << n)
    dp[0] = 1
    
    for h in range(1, 41):
        if h not in hat_to_people:
            continue
        prev_dp = dp.copy()
        people = hat_to_people[h]
        for mask in range(1 << n):
            if prev_dp[mask] == 0:
              