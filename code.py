import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
    
    INF = float('inf')
    dist = [[INF] * (n+1) for _ in range(n+1)]
    
    for u in range(1, n+1):
        q = deque()
        dist_u = [INF] * (n+1)
        dist_u[u] = 0
        q.append(u)
        while q:
            current = q.popleft()
   