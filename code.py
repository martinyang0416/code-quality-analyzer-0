n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n+1)]
count = 0

for i in range(1, n+1):
    a = points[i-1]
    b = points[i % (n+1)]
    c = points[(i+1) % (n+1)]
    abx = b[0] - a[0]
    aby = b[1] - a[1]
    bcx = c[0] - b[0]
    bcy = c[1] - b[1]
    dot = abx * bcx + aby * bcy
    if dot > 0:
        count += 1

print(count)