import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    edges = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    
    # Find all groups (connected components of required nodes)
    group_of = [-1] * N
    current_group = 0
    groups = []
    visited = [False] * N
    for 