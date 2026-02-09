n = int(input())
k = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

min_diff = float('inf')
for i in range(n - k + 1):
    current_diff = arr[i + k - 1] - arr[i]
    if current_diff < min_diff:
        min_diff = current_diff

print(min_diff)