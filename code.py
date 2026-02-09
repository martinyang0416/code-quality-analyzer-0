import sys
from collections import defaultdict

def main():
    kx, ky = map(int, sys.stdin.readline().split())
    rook_positions = set()
    rooks = {}
    rows = defaultdict(int)
    cols = defaultdict(int)
    for i in range(666):
        x, y = map(int, sys.stdin.readline().split())
        rooks[i+1] = (x, y)
        rook_positions.add((x, y))
        rows[x] += 1
        cols[y] += 1

    current_king = (kx, ky)
    for _ in range(2000):
        kx, ky = current_king
        best_move = N