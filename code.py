# Read and normalize all rectangles
normalized = []
for _ in range(6):
    h, w = map(int, input().split())
    if h > w:
        h, w = w, h
    normalized.append((h, w))

# Count occurrences of each normalized rectangle
from collections import defaultdict
counts = defaultdict(int)
for pair in normalized:
    counts[pair] += 1

# Check all counts are even
for k in counts:
    if counts[k] % 2 != 0:
        print("no")
        exit()

# Check total number of pairs is 3
total_pairs = sum(v // 2 f