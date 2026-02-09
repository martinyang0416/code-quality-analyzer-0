import heapq
import math

def main():
    n = int(input())
    d, alpha_deg = map(float, input().split())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    max_count = 1
    heap = []
    best_states = {}
    
    # Initialize the starting point (current=0, prev=None, distance=0, count=1)
    start_current = 0
    start_prev = None
    start_dist = 0.0
    start_count = 1
    heapq.heappush(heap, (-start_count, start_dist, star