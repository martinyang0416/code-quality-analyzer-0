def minFlipsMonoIncr(s: str) -> int:
    n = len(s)
    prefix_ones = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_ones[i] = prefix_ones[i - 1] + (1 if s[i - 1] == '1' else 0)
    
    suffix_zeros = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_zeros[i] = suffix_zeros[i + 1] + (1 if s[i] == '0' else 0)
    
    min_flips = float('inf')
    for i in range(n + 1):
        current = prefix_ones[i] + suffix_zeros[i]
        if current < min_flips:
            min_fli