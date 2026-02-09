n = int(input())
a = list(map(int, input().split()))

even_single = 0
prefix = 0
counts = {0: 1}
result = 0

for num in a:
    cnt = bin(num).count('1')
    if cnt % 2 == 0:
        even_single += 1
    prefix = (prefix + cnt) % 2
    result += counts.get(prefix, 0)
    counts[prefix] = counts.get(prefix, 0) + 1

result -= even_single
print(result)