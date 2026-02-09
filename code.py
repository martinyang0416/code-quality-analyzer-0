import sys
from collections import defaultdict

def main():
    n, m = map(int, sys.stdin.readline().split())
    rows = [sys.stdin.readline().strip() for _ in range(n)]
    
    freq = defaultdict(int)
    for j in range(m):
        c = 0
        for i in range(n):
            if rows[i][j] == '1':
                c |= 1 << i
        freq[c] += 1
    
    max_mask = (1 << n) - 1
    bit_count = [0] * (max_mask + 1)
    for x in range(max_mask + 1):
        bit_count[x] = bin(x).count('1')
    
