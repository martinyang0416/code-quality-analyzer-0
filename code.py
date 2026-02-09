import sys
from collections import defaultdict

def main():
    N = int(sys.stdin.readline())
    counts = defaultdict(int)
    initial_max = 0

    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        k = a + b
        counts[k] += 1
        if k > initial_max:
            initial_max = k

    current_max = initial_max
    k = 0

    while k <= current_max:
        cnt = counts.get(k, 0)
        carry = cnt // 2
        rem = cnt % 2
        counts[k] = rem
        i