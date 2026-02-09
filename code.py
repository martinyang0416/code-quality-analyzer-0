n, k, m = map(int, input().split())
coins = list(map(int, input().split()))

max_total = float('-inf')

for L in range(0, k + 1):
    for R in range(0, k - L + 1):
        if L + R > n:
            continue
        if R == 0:
            selected = coins[:L]
        elif L == 0:
            selected = coins[-R:]
        else:
            selected = coins[:L] + coins[-R:]
        sum_total = sum(selected)
        sorted_selected = sorted(selected)
        x_max = min(m, len(sorted_selected))
    