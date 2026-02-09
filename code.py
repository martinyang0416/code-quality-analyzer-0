import sys
from collections import deque

def main():
    n, k = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    
    # BFS to build parent array with root at n
    parent = [0] * (n + 1)
    visited = [False] * (n + 1)
    q = deque()
    q.append(n)
    visited[n] = True
    parent[n] = -1  # root has no parent
    
    while q:
    