mod = 10**9 + 7

n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# Calculate sum for x coordinates
sum_x = 0
prefix_sum = [0] * n
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + x[i-1]
for j in range(1, n):
    sum_x += x[j] * j - prefix_sum[j]
sum_x %= mod

# Calculate sum for y coordinates
sum_y = 0
prefix_sum_y = [0] * m
for i in range(1, m):
    prefix_sum_y[i] = prefix_sum_y[i-1] + y[i-1]
for j in range(1, m):
    sum_y +