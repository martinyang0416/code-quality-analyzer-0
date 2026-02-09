MOD = 10**9 + 7

n, k = map(int, input().split())
m = n + k - 1

fact = [1] * (m + 1)
for i in range(1, m + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (m + 1)
inv_fact[m] = pow(fact[m], MOD - 2, MOD)
for i in range(m - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

if k == 0:
    print(1)
else:
    if m < k:
        print(0)
    else:
        res = fact[m] * inv_fact[k] % MOD
        res = res * inv_fact[m - k] % MOD
        print(res)