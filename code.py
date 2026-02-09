n, m = map(int, input().split())
bulbs = set()

for _ in range(n):
    parts = list(map(int, input().split()))
    if parts[0] > 0:
        bulbs.update(parts[1:])

print("YES" if len(bulbs) == m else "NO")