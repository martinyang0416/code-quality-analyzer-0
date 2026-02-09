import math

def count_trailing_zeros(n):
    count = 0
    divisor = 5
    while divisor <= n:
        count += n // divisor
        divisor *= 5
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 1:
        print(1)
        continue
    k = count_trailing_zeros(n)
    if n == 0:
        log_fact = 0.0
    else:
        log_fact = (n * math.log(n) - n + 0.5 * math.log(2 * math.pi * n)) / math.log(10)
    s = log_fact - k
    digits = int(s) + 1
    print(digi