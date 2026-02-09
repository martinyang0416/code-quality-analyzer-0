import sys
from collections import deque

MOD = 10**9 + 7

def main():
    n = int(sys.stdin.readline())
    values = list(map(int, sys.stdin.readline().split()))
    edges = [[] for _ in range(n+1)]  # 1-based indexing
    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)
    
    # BFS to find parent and order
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    order = []
    q = deque()
    q.append(1)
 