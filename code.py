n = int(input())
m = 2 * n - 2
total = 0

for i in range(m - n + 1):
    # Calculate the number of edges
    edges = 0
    if i > 0:
        edges += 1
    if i + n < m:
        edges += 1
    
    # Calculate the number of remaining lamps
    remaining = m - n - edges
    ways = 4 * (3 ** edges) * (4 ** remaining)
    total += ways

print(total)