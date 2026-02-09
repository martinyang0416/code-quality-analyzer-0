import sys
from collections import defaultdict

def main():
    n, m = map(int, sys.stdin.readline().split())
    if m % 2 != 0:
        print("No solution")
        return
    
    edges = []
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append((v, len(edges)-1))
        adj[v].append((u, len(edges)-1))
    
    used = [False] * m
    ans = []
    visited = [False] * (n + 1)
    parent = {}
  