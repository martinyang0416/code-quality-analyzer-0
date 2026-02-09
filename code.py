initial_elements = list(map(int, input().split()))

blocks = []
current_size = 0

for num in reversed(initial_elements):
    current_size += 1
    if blocks and blocks[0][0] == num:
        blocks[0] = (num, blocks[0][1] + 1)
    else:
        blocks.insert(0, (num, 1))

import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    if parts[0] == 'L':
        X = int(parts[1])
        Y = int(parts[2])
        current_size += X
        