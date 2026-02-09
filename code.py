n = int(input())
shop_masks = []
for _ in range(n):
    f = list(map(int, input().split()))
    mask = 0
    for j in range(10):
        if f[j]:
            mask |= 1 << j
    shop_masks.append(mask)
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))
max_total = -float('inf')
for joisino_mask in range(1, 1 << 10):
    total = 0
    for i in range(n):
        overlap = joisino_mask & shop_masks[i]
        c = bin(overlap).count('1')
        total += p[i][c]
    if total > ma