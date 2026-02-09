def minTaps(n, ranges):
    max_reach = [0] * (n + 1)
    for i in range(n + 1):
        r = ranges[i]
        s = max(0, i - r)
        e = min(n, i + r)
        if s > e:
            continue
        max_reach[s] = max(max_reach[s], e)
    
    current_end = 0
    next_end = 0
    taps = 0
    
    for i in range(n + 1):
        if i > next_end:
            return -1
        next_end = max(next_end, max_reach[i])
        if i == current_end:
            if current_end >= n:
                bre