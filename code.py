MOD = 10**9 + 7

P, Q = map(int, input().split())

result = pow(Q + 1, P, MOD) * pow(P + 1, Q, MOD) % MOD
print(result)