def minSteps(n):
    if n == 1:
        return 0
    res = 0
    d = 2
    while d * d <= n:
        while n % d == 0:
            res += d
            n = n // d
        d += 1
    if n > 1:
        res += n
    return res