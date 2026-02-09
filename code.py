import sys
from sys import stdin
from sys import setrecursionlimit

def main():
    sys.setrecursionlimit(1 << 25)
    n, m, k = map(int, stdin.readline().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    
    visited = [False] * (n + 1)
    path_stack = []
    pos = [-1] * (n + 1)
    
    for start in range(1, n+1):
        if not visited[start]:
            stack = [(start,