import sys
from collections import deque

def main():
    lines = [line.strip() for line in sys.stdin if line.strip() != '']
    idx = 0
    t = int(lines[idx])
    idx += 1
    for _ in range(t):
        k, n, m = map(int, lines[idx].split())
        idx += 1
        a = list(map(int, lines[idx].split()))
        idx += 1
        b = list(map(int, lines[idx].split()))
        idx += 1
        
        zeros_a = [0] * (n + 1)
        for i in range(1, n + 1):
            zeros_a[i] = zeros_a[i -