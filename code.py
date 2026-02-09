n = int(input())
products = []
sum_a = 0
for _ in range(n):
    a, b = map(int, input().split())
    products.append((a, b))
    sum_a += a

sum_full = 0
for a, b in products:
    temp = b - (sum_a - a)
    x = max(0, min(a, temp))
    sum_full += x

print(sum_a + sum_full)