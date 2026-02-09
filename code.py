T = int(input())
for _ in range(T):
    n = int(input())
    stats = [tuple(map(int, input().split())) for _ in range(n)]
    valid = True
    # Check if any c_i > p_i
    for p, c in stats:
        if c > p:
            valid = False
            break
    if not valid:
        print("NO")
        continue
    # Check consecutive entries
    for i in range(1, n):
        prev_p, prev_c = stats[i-1]
        curr_p, curr_c = stats[i]
        if curr_p < prev_p or curr_c < prev_c:
            valid