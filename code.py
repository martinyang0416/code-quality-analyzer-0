import sys
from sys import stdin
from collections import defaultdict

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(stdin.readline())
    p = list(map(int, stdin.readline().split()))  # p is 1-based element values

    # Decompose into cycles
    visited = [False] * (n + 1)
    cycles = []
    for i in range(1, n + 1):
        if not visited[i]:
            current = i
            cycle = []
            while not visited[current]:
                visited[current] = True
            