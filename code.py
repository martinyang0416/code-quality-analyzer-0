from collections import deque

n, m = map(int, input().split())
p = list(map(int, input().split()))
target = p[-1]

# Build reversed adjacency list
adj_reversed = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_reversed[v].append(u)

# BFS to find reachable nodes in reversed graph
reachable = [False] * (n + 1)
q = deque([target])
reachable[target] = True

while q:
    u = q.popleft()
    for v in adj_reversed[u]:
        if not reachable[v]:
           