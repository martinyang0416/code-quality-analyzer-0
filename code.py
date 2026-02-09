import bisect
from collections import deque

n, k, l = map(int, input().split())
x = list(map(int, input().split()))
a_list = list(map(int, input().split()))

x.sort()
x_set = set(x)
unique_a = list(set(a_list))

mask_set = set()

for a in unique_a:
    if a > n:
        continue
    max_s = n - a + 1
    if max_s < 1:
        continue
    for s in range(1, max_s + 1):
        e = s + a - 1
        if e > n:
            continue
        if s not in x_set or e not in x_set:
            continue
 