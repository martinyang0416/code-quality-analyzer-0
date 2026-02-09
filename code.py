k, n = map(int, input().split())
times = list(map(int, input().split()))
times.sort()

gaps = []
for i in range(n - 1):
    gaps.append((times[i + 1] - times[i], i))

gaps.sort()

selected = set()
total = 0
count = 0

for gap, idx in gaps:
    if count >= k:
        break
    if idx in selected:
        continue
    if (idx - 1 in selected) or (idx + 1 in selected):
        continue
    selected.add(idx)
    total += gap
    count += 1

print(total)