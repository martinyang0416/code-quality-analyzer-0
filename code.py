n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

robots = sorted(zip(x, v), key=lambda r: r[0])

low = robots[0][0]
high = robots[-1][0]

epsilon = 1e-12
iterations = 100

for _ in range(iterations):
    if high - low < epsilon:
        break
    mid1 = low + (high - low) / 3
    mid2 = high - (high - low) / 3
    f1 = max(abs(xi - mid1) / vi for xi, vi in robots)
    f2 = max(abs(xi - mid2) / vi for xi, vi in robots)
    if f1 < f2:
        high = mid2
 