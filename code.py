import heapq

def minCost(grid):
    m = len(grid)
    n = len(grid[0])
    if m == 1 and n == 1:
        return 0
    dirs = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = 0
    target = (m-1, n-1)
    
    while heap:
        cost, i, j = heapq.heappop(heap)
        if (i, j) == target:
            return cost
        if cost > dist[i][j]:
            continue
        original_d