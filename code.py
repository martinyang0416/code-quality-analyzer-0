import math

def nthMagicalNumber(N: int, A: int, B: int) -> int:
    MOD = 10**9 + 7
    g = math.gcd(A, B)
    lcm = (A * B) // g
    low, high = 1, N * max(A, B)
    
    while low < high:
        mid = (low + high) // 2
        count = mid // A + mid // B - mid // lcm
        if count < N:
            low = mid + 1
        else:
            high = mid
    return low % MOD