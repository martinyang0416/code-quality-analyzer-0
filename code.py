import sys
from collections import defaultdict

def precompute_spf(max_num):
    spf = list(range(max_num + 1))  # Initialize each number as its own spf
    for i in range(2, int(max_num**0.5) + 1):
        if spf[i] == i:  # i is a prime
            for j in range(i * i, max_num + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

max_a = 200000
spf = precompute_spf(max_a)

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    