n, k = map(int, input().split())
ids = list(map(int, input().split()))

low, high = 1, n
while low < high:
    mid = (low + high) // 2
    s = mid * (mid + 1) // 2
    if s >= k:
        high = mid
    else:
        low = mid + 1

m = low
sum_prev = (m - 1) * m // 2
index = k - sum_prev - 1
print(ids[index])