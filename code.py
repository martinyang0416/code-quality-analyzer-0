# Precompute the factorial values up to 10! since L can be at most 10
fact = [1] * (11)
for i in range(1, 11):
    fact[i] = fact[i-1] * i

# LED counts for each digit
digit_led = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

def solve():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        L = int(input[idx])
        M = int(input[idx+1])
        idx += 2
        
        to