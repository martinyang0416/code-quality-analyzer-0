n = int(input())
total = 0
for a in range(1, n):
    total += (n - 1) // a
print(total)