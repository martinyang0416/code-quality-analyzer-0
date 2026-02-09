import sys
from functools import lru_cache

n = int(sys.stdin.readline())
grid = [sys.stdin.readline().strip() for _ in range(n)]

@lru_cache(maxsize=None)
def dfs(r, c, d):
    if r == n and c == n:
        return d
    current_player = (r + c) % 2
    moves = []
    if r < n:
        next_char = grid[r][c-1]  # (r+1, c) in 1-based -> grid[r][c-1] in 0-based
        delta = 1 if next_char == 'a' else (-1 if next_char == 'b' else 0)
        moves.append(dfs(r + 1, c, d + delta))
    if c < n:
  