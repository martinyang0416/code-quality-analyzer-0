n, *rest = map(int, open(0).read().split())
a = rest[:n]
mod = n - 1
remainder_map = {}
for num in a:
    r = num % mod
    if r in remainder_map:
        print(remainder_map[r], num)
        break
    remainder_map[r] = num