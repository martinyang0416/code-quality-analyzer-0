def sieve(n):
    if n < 2:
        return []
    sieve_list = [True] * (n + 1)
    sieve_list[0], sieve_list[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if sieve_list[i]:
            sieve_list[i*i : n+1 : i] = [False] * len(sieve_list[i*i : n+1 : i])
    primes = [i for i, is_prime in enumerate(sieve_list) if is_prime]
    return primes

def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        C, D