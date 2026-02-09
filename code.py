n = int(input())
ropes = list(map(int, input().split()))
from collections import Counter

freq = Counter(ropes)
total_loops = 0

for count in freq.values():
    total_loops += count // 3

print(total_loops)