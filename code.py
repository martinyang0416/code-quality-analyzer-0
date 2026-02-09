n, k, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

min_time = float('inf')

for s in range(len(b) - n + 1):
    current_max = 0
    for i in range(n):
        time = abs(a[i] - b[s + i]) + abs(b[s + i] - p)
        current_max = max(current_max, time)
    min_time = min(min_time, current_max)

print(min_time)