from typing import List
from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        start_x, start_y = -1, -1
        key_count = 0
        
        # Find the starting position and count the keys
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == '@':
                    start_x, start_y = i, j
                el