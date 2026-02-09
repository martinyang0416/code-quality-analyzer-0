n, m = map(int, input().split())
v = list(map(int, input().split()))
total = 0
for _ in range(m):
    x, y = map(int, input().split())
    total += min(v[x-1], v[y-1])
print(total)