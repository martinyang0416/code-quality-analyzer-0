MOD = 10**9 + 7
inv2 = 500000004  # Modular inverse of 2 under MOD

n = int(input())
res = (n * inv2) % MOD
print('\n'.join([str(res)] * n))