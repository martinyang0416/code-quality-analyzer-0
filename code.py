def numDupDigitsAtMostN(N):
    if N < 1:
        return 0
    digits = list(map(int, str(N)))
    n_length = len(digits)
    
    sum_lesser = 0
    for l in range(1, n_length):
        if l == 1:
            sum_lesser += 9
        else:
            product = 9
            available = 9
            for i in range(1, l):
                product *= available
                available -= 1
            sum_lesser += product
    
    from functools import lru_cache
    @lru_cache(maxsize=None)
    