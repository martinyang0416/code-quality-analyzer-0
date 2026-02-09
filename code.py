import math

n = int(input())
for _ in range(n):
    ai = input().strip()
    found = False
    for k in range(1, 100001):
        # Calculate the number of digits in 2^k
        m = int(k * math.log10(2)) + 1
        l = min(m, 100)
        mod = 10 ** l
        last_l = pow(2, k, mod)
        last_str = str(last_l).zfill(l)
        if ai in last_str:
            print(k)
            found = True
            break
    if not found:
        # In case not found, fallback to a large exponent (thou