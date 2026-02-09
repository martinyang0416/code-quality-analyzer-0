import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    cow = [i+1 for i in range(N) if s[i] == '1']
    T = len(cow)
    if T == 0:
        exit()

    edges = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)

    # Find M and M_sum (number of cow components and their total size)
 