import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    found = False
    for k in range(2, n):
        if a[0] + a[1] <= a[k]:
            print(1, 2, k+1)
            found = True
            break
    if not found:
        print(-1)