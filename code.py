import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    edges = [[] for _ in range(N+1)]  # 1-based
    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)
    
    selected = []
    for i in range(N):
        if s[i] == '1':
            selected.append(i+1)  # nodes are 1-based
    
    # Step 1: Find the Steiner