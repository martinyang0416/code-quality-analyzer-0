import math

def count_reward_days(d):
    S = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(S)
    total = 0

    for mask in range(1, 1 << n):
        bits = bin(mask).count('1')
        elements = []
        for i in range(n):
            if mask & (1 << i):
                elements.append(S[i])
        current_lcm = 1
        for num in elements:
            current_lcm = current_lcm * num // math.gcd(current_lcm, num)
            if current_lcm > d:
                break
        if current_