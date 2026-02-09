MOD = 10**9 + 7

n = int(input())

if n < 2:
    print(0)
else:
    # Compute factorial(n) mod MOD
    fact = 1
    for i in range(2, n + 1):
        fact = (fact * i) % MOD
    
    # Compute 2^(n-1) mod MOD
    pow2 = pow(2, n - 1, MOD)
    
    # Calculate the result
    result = (fact - pow2) % MOD
    print(result)