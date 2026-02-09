n = int(input())
hero = list(map(int, input().split()))
h0, a0, d0, s0 = hero
enemies = []
for _ in range(n):
    h, a, d, s = map(int, input().split())
    enemies.append((h, a, d, s))

# Check if any enemy cannot be killed
for h, a, d, s in enemies:
    delta = a0 - d
    if delta <= 0 and h > 0:
        print(-1)
        exit()

valid_enemies = []
sum_part2 = 0

for h, a, d, s in enemies:
    delta = a0 - d
    damage = max(a - d0, 0)
    if damage == 0:
        continue
    k = (h + delta - 