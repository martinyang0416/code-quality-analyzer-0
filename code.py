n = int(input())
a = list(map(int, input().split()))
min_time = float('inf')

for k in range(n + 1):
    if k == 0:
        current = 10**6 - a[0]
    elif k == n:
        current = a[-1] - 1
    else:
        my_time = a[k-1] - 1
        friend_time = 10**6 - a[k]
        current = max(my_time, friend_time)
    if current < min_time:
        min_time = current

print(min_time)