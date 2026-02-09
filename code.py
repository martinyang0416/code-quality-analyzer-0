n, m = map(int, input().split())
total = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    total += a + b + c
print(total % 97)