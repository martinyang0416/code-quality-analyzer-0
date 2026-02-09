import bisect

n = int(input())
t = list(map(int, input().split()))
t.sort()
max_len = 0

for i in range(n):
    a = t[i]
    b = a + 2
    j = bisect.bisect_right(t, b)
    current_len = j - i
    if current_len > max_len:
        max_len = current_len

print(max_len)