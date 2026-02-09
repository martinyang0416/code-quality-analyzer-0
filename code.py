n = int(input())
result = 0
for x in range(1, n):
    result += (n - 1) // x
print(result)