from collections import Counter

n = int(input())
given = [int(input()) for _ in range(n)]

for m in range(1, 167):
    a = m
    d = 3 * m
    # Check if all given numbers are between m and 3m
    if any(num < a or num > d for num in given):
        continue
    # Generate all possible x values
    for x in range(a, 2 * m + 1):
        y = 4 * m - x
        if y < x or y > d:
            continue  # Ensure y is within bounds
        four_set = [a, x, y, d]
        four_freq = Counter(four_set)
