n = int(input())
if n == 2:
    print("YES")
    exit()

degrees = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    degrees[u] += 1
    degrees[v] += 1

for i in range(1, n + 1):
    if degrees[i] == 1:
        continue
    if degrees[i] < 3:
        print("NO")
        exit()

print("YES")