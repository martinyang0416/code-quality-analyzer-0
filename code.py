import heapq
from collections import defaultdict

def main():
    n, m, k, c, d = map(int, input().split())
    a = list(map(int, input().split()))
    streets = []
    for _ in range(m):
        x, y = map(int, input().split())
        streets.append((x, y))
    
    directed_edges = defaultdict(list)
    for x, y in streets:
        directed_edges[x].append(y)
        directed_edges[y].append(x)
    
    edge_counts = defaultdict(int)
    total_discontent = 0
    T_max = 200  # Sufficiently la