n = int(input())
if n < 3:
    print(0)
else:
    degrees = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        degrees[u] += 1
        degrees[v] += 1
    total = n * (n - 1) * (n - 2) // 6
    sum_edges = (n - 1) * (n - 2)
    sum_pairs = sum(d * (d - 1) // 2 for d in degrees)
    result = total - sum_edges + sum_pairs
    print(max(0, result))