n, q = map(int, input().split())

lower = [1] * (n + 1)  # 1-based indexing
upper = [n] * (n + 1)

for _ in range(q):
    t, l, r, v = map(int, input().split())
    if t == 1:
        # At least v, update lower bound
        for i in range(l, r + 1):
            if lower[i] < v:
                lower[i] = v
    else:
        # At most v, update upper bound
        for i in range(l, r + 1):
            if upper[i] > v:
                upper[i] = v

# Check for feasibility
possible = True
for i in