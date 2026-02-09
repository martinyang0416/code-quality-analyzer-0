def find_prime_pair(m):
    # Sieve of Eratosthenes to find all primes up to m
    sieve = [True] * (m + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(m ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i : m+1 : i] = [False] * len(sieve[i*i : m+1 : i])
    
    # Find the first pair (a, b) such that a + b = m and both are primes
    for a in range(2, m // 2 + 1):
        b = m - a
        if sieve[a] and sieve[b]:
            return (a, b)
    return (None, None)  # This lin