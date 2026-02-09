import math

t = int(input())
for _ in range(t):
    n1 = int(input())
    n2 = int(input())
    k = int(input())
    max_gcd = 0
    for a in range(max(1, n1 - k), n1 + k + 1):
        steps_a = abs(a - n1)
        if steps_a > k:
            continue
        rem_steps = k - steps_a
        min_b = max(1, n2 - rem_steps)
        max_b = n2 + rem_steps
        for b in range(min_b, max_b + 1):
            steps_b = abs(b - n2)
            if steps_a + steps_b > k:
                continue
      