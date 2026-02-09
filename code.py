MOD = 998244353

n = int(input())
primes = list(map(int, input().split()))

from collections import defaultdict
count = defaultdict(int)
for p in primes:
    count[p] += 1

exponents = list(count.values())
sum_e = sum(exponents)
s = sum_e // 2

result = 1
for e in exponents:
    lower = max(0, s - (sum_e - e))
    upper = min(e, s)
    if upper < lower:
        result = 0
        break
    result = (result * (upper - lower + 1)) % MOD

print(result)