m = list(map(int, input().split()))
w = list(map(int, input().split()))
hs, hu = map(int, input().split())

total_score = 0

for i in range(5):
    x = 500 * (i + 1)
    mi = m[i]
    wi = w[i]
    part1 = 0.3 * x
    part2 = x * (1 - mi / 250) - 50 * wi
    total_score += max(part1, part2)

total_score += 100 * hs - 50 * hu
print(int(total_score))