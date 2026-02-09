import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    in_deg = [0] * (n + 1)
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        in_deg[v] += 1
    
    q = deque()
    for i in range(1, n + 1):
        if in_deg[i] == 0:
            q.append(i)
    
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
 