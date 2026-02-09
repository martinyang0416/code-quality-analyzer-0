import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n+1)]
for u in range(1, n+1):
    parts = list(map(int, sys.stdin.readline().split()))
    ci = parts[0]
    adj[u] = parts[1:ci+1]

s = int(sys.stdin.readline())

terminal = [False] * (n+1)
for u in range(1, n+1):
    if len(adj[u]) == 0:
        terminal[u] = True

# Step 1: BFS to find winning path
visited = [[False]*(n+1) for _ in range(2)]
prev = [[None]*(n+1) for _ in range(2)]
