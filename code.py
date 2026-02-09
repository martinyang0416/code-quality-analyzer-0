import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    max_l = 0
    min_r = float('inf')
    for _ in range(n):
        l, r = map(int, sys.stdin.readline().split())
        if l > max_l:
            max_l = l
        if r < min_r:
            min_r = r
    print(max(0, max_l - min_r))