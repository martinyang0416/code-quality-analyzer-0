import sys
from collections import defaultdict

def main():
    m = int(sys.stdin.readline())
    edges = []
    outgoing = defaultdict(list)

    for idx in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        outgoing[u].append(idx)
    
    max_degree = 0
    for u in outgoing:
        current = len(outgoing[u])
        if current > max_degree:
            max_degree = current
    
    k = max_degree
    colors = [0] * m

    for u in outgoing:
